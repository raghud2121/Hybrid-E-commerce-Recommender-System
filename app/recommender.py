from .models import models
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self):
        self.corr_matrix = models.corr_matrix
        self.user_id_map_cf = models.user_id_map_cf
        self.user_code_map_cf = models.user_code_map_cf
        self.df_sample = models.df_sample
        
        self.tfidf = models.tfidf
        self.item_features = models.item_features
        self.item_id_map = models.item_id_map

    def get_collaborative_recs(self, user_id, n=10):
        # Check if the user exists in our model
        if user_id not in self.user_code_map_cf:
            return []

        # Get the integer code for the user
        user_code = self.user_code_map_cf[user_id]
        
        # Get similarity scores for this user against all others
        user_similarities = self.corr_matrix[user_code]
        
        # Find top N similar users (excluding the user themselves)
        similar_user_codes = user_similarities.argsort()[-n-1:-1][::-1]
        
        # Get the string IDs of these similar users
        similar_user_ids = [self.user_id_map_cf[code] for code in similar_user_codes]

        # Get items rated highly by these similar users
        recs = self.df_sample[self.df_sample['user_id'].isin(similar_user_ids)]
        recs = recs[recs['rating'] >= 4.0]['item_id'].unique()
        
        # Remove items the target user has already rated
        items_rated_by_user = self.df_sample[self.df_sample['user_id'] == user_id]['item_id']
        final_recs = [rec for rec in recs if rec not in items_rated_by_user.values]
        
        return final_recs[:n]

    def get_content_recs(self, item_id, n=10):
        try:
            # This function remains the same
            idx = self.item_id_map[self.item_id_map == item_id].index[0]
            cosine_sim = cosine_similarity(self.item_features[idx], self.item_features)
            sim_scores = list(enumerate(cosine_sim[0]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:n+1]
            item_indices = [i[0] for i in sim_scores]
            return self.item_id_map.iloc[item_indices].tolist()
        except IndexError:
            return []

    def get_hybrid_recs(self, user_id, n=10):
        collab_recs = self.get_collaborative_recs(user_id, n)
        
        user_ratings = self.df_sample[self.df_sample['user_id'] == user_id]
        if not user_ratings.empty:
            top_item_id = user_ratings.sort_values('rating', ascending=False).iloc[0]['item_id']
            content_recs = self.get_content_recs(top_item_id, n)
        else:
            content_recs = []

        hybrid_recs = list(dict.fromkeys(collab_recs + content_recs))
        return hybrid_recs[:n]

reco_engine = Recommender()