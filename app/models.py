import pickle
import pandas as pd

class ModelLoader:
    def __init__(self):
        print("Loading models...")
        self.corr_matrix = pickle.load(open('saved_models/corr_matrix.pkl', 'rb'))
        self.user_id_map_cf = pickle.load(open('saved_models/user_id_map_cf.pkl', 'rb'))
        self.df_sample = pd.read_pickle('saved_models/df_sample.pkl')
        
        # Invert the map for easy lookups from user_id to code
        self.user_code_map_cf = {v: k for k, v in self.user_id_map_cf.items()}

        # Content-based models from Cell 3
        self.tfidf = pickle.load(open('saved_models/tfidf_vectorizer.pkl', 'rb'))
        self.item_features = pickle.load(open('saved_models/item_features.pkl', 'rb'))
        self.item_id_map = pd.read_pickle('saved_models/item_id_map.pkl')
        print("Models loaded successfully!")

models = ModelLoader()