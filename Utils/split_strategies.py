"""
Splitting classes into seen/unseen sets.
"""

import numpy as np

class ClassSplitter:
    """Manages different strategies for splitting classes into seen/unseen sets."""
    
    def __init__(self, random_seed=22):
        """
        Initialize class splitter.
        """
        self.random_seed = random_seed
        np.random.seed(random_seed)
    
    def split_random(self, all_classes, seen_ratio=0.5):
        """
        Random split of classes.
        """
        if not 0.0 < seen_ratio < 1.0:
            raise ValueError("seen_ratio must be between 0 and 1.")
        
        all_classes = np.array(all_classes)
        np.random.shuffle(all_classes)
        
        n_seen = int(len(all_classes) * seen_ratio)
        seen_classes = all_classes[:n_seen].tolist()
        unseen_classes = all_classes[n_seen:].tolist()
        
        return sorted(seen_classes), sorted(unseen_classes)