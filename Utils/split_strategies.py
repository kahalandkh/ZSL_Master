"""
Splitting classes into seen/unseen sets.
"""

import numpy as np
import pandas as pd


class ClassSplitter:
    """Manages different strategies for splitting classes into seen/unseen sets."""
    
    def __init__(self, random_seed=22):
        """
        Initialize class splitter.
        
        Args:
            random_seed: Random seed for reproducibility
        """
        self.random_seed = random_seed
        np.random.seed(random_seed)
    
    def split_random(self, all_classes, seen_ratio = 0.5):
        """
        Random split of classes.
        """
        all_classes = np.array(all_classes)
        np.random.shuffle(all_classes)
        
        n_seen = int(len(all_classes) * seen_ratio)
        seen_classes = all_classes[:n_seen].tolist()
        unseen_classes = all_classes[n_seen:].tolist()
        
        return sorted(seen_classes), sorted(unseen_classes)