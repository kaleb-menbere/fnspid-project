import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF

class TextAnalyzer:
    """Perform NLP analysis and topic modeling on financial headlines"""
    
    def __init__(self):
        self.corpus = None
        self.corpus_clean = None
        self.tfidf_vectorizer = None
        self.nmf_model = None
        self.feature_names = None
    
    def preprocess_text(self, text_series):
        """Clean and preprocess text data"""
        self.corpus = text_series.astype(str).fillna('')
        
        def clean_text(text):
            text = text.lower()
            text = re.sub(r'[^a-z0-9\s]', '', text)
            text = re.sub(r'\s+', ' ', text)
            return text.strip()
        
        self.corpus_clean = self.corpus.apply(clean_text)
        return self.corpus_clean
    
    def vectorize_text(self, max_features=20000):
        """Create TF-IDF matrix"""
        self.tfidf_vectorizer = TfidfVectorizer(
            max_df=0.95, min_df=5, ngram_range=(1,2), 
            stop_words='english', max_features=max_features
        )
        X_tfidf = self.tfidf_vectorizer.fit_transform(self.corpus_clean)
        self.feature_names = np.array(self.tfidf_vectorizer.get_feature_names_out())
        return X_tfidf
    
    def perform_topic_modeling(self, n_topics=10):
        """Perform NMF topic modeling"""
        X_tfidf = self.vectorize_text()
        
        self.nmf_model = NMF(n_components=n_topics, random_state=42, max_iter=200)
        W = self.nmf_model.fit_transform(X_tfidf)  # document-topic matrix
        H = self.nmf_model.components_             # topic-term matrix
        
        return W, H
    
    def get_top_keywords(self, n_keywords=50):
        """Get top keywords by average TF-IDF"""
        X_tfidf = self.vectorize_text()
        avg_tfidf = np.asarray(X_tfidf.mean(axis=0)).ravel()
        top_idx = avg_tfidf.argsort()[::-1][:n_keywords]
        return self.feature_names[top_idx]
    
    def assign_topics(self, df):
        """Assign dominant topic to each document"""
        W, H = self.perform_topic_modeling()
        df['dominant_topic'] = W.argmax(axis=1)
        return df