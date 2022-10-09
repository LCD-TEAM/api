import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_recom(target: int, role_vector: np.array, place: int, vectors: np.array, clusters: np.array, data):
    rating = np.argsort(cosine_similarity(vectors[clusters == target], role_vector).reshape(-1))
    rang = np.arange(len(rating))
    return data.iloc[rang[rating == place][0]]

def recommend_buh(n: int):
    df = pd.read_csv('models/data.csv')
    clusters = df['clusters']

    with open('models/vector_buh', 'rb') as f:
        role_vector = pickle.load(f)
    
    with open('models/reduced_vect', 'rb') as f:
        vectors = pickle.load(f)

    target = 7

    news = []
    for p in range(n):
        recom_news = get_recom(target, role_vector, p, vectors, clusters, df)
        news.append(dict(recom_news[['title', 'content', 'date', 'tags']]))

    return news

def recommend_gen(n: int):
    df = pd.read_csv('models/data.csv')
    clusters = df['clusters']

    with open('models/vector_gen', 'rb') as f:
        role_vector = pickle.load(f)
    
    with open('models/reduced_vect', 'rb') as f:
        vectors = pickle.load(f)

    target = 2

    news = []
    for p in range(n):
        recom_news = get_recom(target, role_vector, p, vectors, clusters, df)
        news.append(dict(recom_news[['title', 'content', 'date', 'tags']]))

    return news

def recommend(role: str):
    if role.lower() == 'бухгалтер':
        return recommend_buh(3)
    elif role.lower() == 'ген. директор':
        return recommend_gen(3)