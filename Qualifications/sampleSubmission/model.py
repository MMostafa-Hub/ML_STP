import numpy as np

class Model:
    def __init__(self):
        # Create model and load weights
        self.classes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        
    def predict(self,sentence):
        return np.random.choice(self.classes)
