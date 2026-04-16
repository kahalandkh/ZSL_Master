"""
Generating and managing embeddings for different embedding models and activity description types.
"""
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoModel, AutoTokenizer, CLIPModel, CLIPTokenizer

device = torch.device("cuda" if torch.cuda.is_available() else ('mps' if torch.backends.mps.is_available() else "cpu"))


class EmbeddingGenerator:
    """Generate and manage embeddings for different models and activity description types."""
    
    MODELS = [
        'all-MiniLM-L6-v2',
        'all-mpnet-base-v2',
        'all-MiniLM-L12-v2',
        'clip-ViT-B/32',
        'clip-ViT-L/14',
        'hkunlp/instructor-large',
        'bert-base-uncased',
        'paraphrase-MiniLM-L6-v2' # originally used in "Recognizing Hand-based Micro Activities Using Wrist-Worn Inertial Sensors: A Zero-Shot Learning Approach" (Fadi et. al, 2024)
    ]
    
    
    def __init__(self, output_dir="../Data/Embeddings/"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    
    def _generate_filename(self, model_name, desc_type, use_prompt, dataset='fadi'):
        """Generate a filename for embeddings with format like: {model_name}_{desc_type}_{prompt}_{dataset}.npz"""
        clean_model = model_name.replace('/', '_').replace('-', '_').lower()
        prompt_suffix = "prompt" if use_prompt else "noprompt"
        return f"{clean_model}_{desc_type}_{prompt_suffix}_{dataset}.npz"
    
    
    def generate_embeddings(self, descriptions_dict, model_name, use_prompt=False, device=device):
        """Generate embeddings for given activity descriptions."""
        
        if model_name not in self.MODELS:
            raise ValueError(
                f"Unsupported model: {model_name}."
                f"Supported models: {self.MODELS}"
            )
            
        activities = list(descriptions_dict.keys())
        descriptions = [descriptions_dict[act] for act in activities]
        
        print(f"Loading model: {model_name}")
        base_prompt = "Represent the activity for zero-shot activity recognition: {}"
        
        # CLIP models (Hugging Face transformers)
        if model_name.startswith("clip"):
            hf_model_map = {
                "clip-ViT-B/32": "openai/clip-vit-base-patch32",
                "clip-ViT-L/14": "openai/clip-vit-large-patch14"
            }
            
            hf_model_name = hf_model_map[model_name]
            
            model = CLIPModel.from_pretrained(hf_model_name).to(device)
            tokenizer = CLIPTokenizer.from_pretrained(hf_model_name)
            model.eval()
            
            if use_prompt:
                prompts = [base_prompt.format(desc) for desc in descriptions]
            else:
                prompts = descriptions
                
            print(f"Generating CLIP embeddings for {len(activities)} activities...")
            
            with torch.no_grad():
                inputs = tokenizer(prompts, padding=True, truncation=True, return_tensors="pt").to(device)
                text_features = model.get_text_features(**inputs)

                if hasattr(text_features, "text_embeds"):
                    text_features = text_features.text_embeds
                elif hasattr(text_features, "pooler_output"):
                    text_features = text_features.pooler_output

                text_features = text_features / text_features.norm(dim=-1, keepdim=True)

            embedding_array = text_features.cpu().numpy()
        
        # Instructor models
        elif "instructor" in model_name:
            model = SentenceTransformer(model_name, device=device)
            
            if use_prompt:
                inputs = [[base_prompt, desc] for desc in descriptions]
            else:
                inputs = [["", desc] for desc in descriptions]
            
            print(f"Generating Instructor embeddings for {len(activities)} activities...")
            embedding_array = model.encode(inputs, normalize_embeddings=True, show_progress_bar=True)

        # BERT models
        elif "bert" in model_name and "sentence" not in model_name:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModel.from_pretrained(model_name).to(device)
            model.eval()
            
            print(f"Generating BERT embeddings for {len(activities)} activities...")
            embeddings_list = []
            with torch.no_grad():
                for desc in descriptions:
                    text = base_prompt.format(desc) if use_prompt else desc
                    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
                    outputs = model(**inputs).last_hidden_state
                    mask = inputs["attention_mask"].unsqueeze(-1).expand(outputs.size())
                    mean_pooled = (outputs * mask).sum(1) / mask.sum(1)
                    embeddings_list.append(mean_pooled.squeeze().cpu().numpy())
            
            embedding_array = np.vstack(embeddings_list)
            embedding_array = embedding_array / np.linalg.norm(embedding_array, axis=1, keepdims=True)
        
        # Sentence-Transformers models
        else:
            model = SentenceTransformer(model_name, device=device)
            
            if use_prompt:
                prompts = [base_prompt.format(desc) for desc in descriptions]
            else:
                prompts = descriptions
                
            print(f"Generating Sentence-Transformer embeddings for {len(activities)} activities...")
            embedding_array = model.encode(prompts, normalize_embeddings=True, show_progress_bar=True)
        
        return embedding_array


    def save_embeddings(self, embeddings_array, model_name, desc_type, use_prompt=False, dataset='fadi'):
        """Save embeddings to .npz file"""
        filename = self._generate_filename(model_name, desc_type, use_prompt, dataset)
        filepath = self.output_dir / filename
        
        np.savez_compressed(
            filepath,
            embeddings=embeddings_array,
            model_name=model_name,
            desc_type=desc_type,
            use_prompt=use_prompt,
            dataset=dataset,
            created_at=datetime.now().isoformat()
        )
        
        print(f"Saved embeddings to: {filepath}")
        print(f"Shape: {embeddings_array.shape}")
        print(f"File size: {filepath.stat().st_size / 1024:.1f} KB")
        
        return filepath


    def load_embeddings(self, model_name, desc_type, use_prompt=False, dataset='fadi'):
        """Load embeddings as numpy array."""
        filename = self._generate_filename(model_name, desc_type, use_prompt, dataset)
        filepath = self.output_dir / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"No embeddings found at {filepath}")
        
        data = np.load(filepath, allow_pickle=True)
        
        print(f"Loaded embeddings from: {filepath}")
        print(f"Model: {data['model_name']}")
        print(f"Shape: {data['embeddings'].shape}")
        
        return data['embeddings']

      
    def generate_and_save(self, descriptions_dict, model_name, desc_type, use_prompt=False, dataset='fadi'):
        """Generate and save embeddings in one step."""
        embeddings = self.generate_embeddings(descriptions_dict, model_name, use_prompt=use_prompt, device=device)
        filepath = self.save_embeddings(embeddings, model_name, desc_type, use_prompt, dataset)
        return embeddings, filepath