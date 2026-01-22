import numpy as np
from sentence_transformers import SentenceTransformer
from numpy.linalg import norm

# Load stored data
embeddings = np.load("embeddings.npy")
documents = np.load("documents.npy")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))

query = input("Enter your search query: ")

query_embedding = model.encode(query)

scores = [
    cosine_similarity(query_embedding, emb)
    for emb in embeddings
]

best_match_index = np.argmax(scores)

print("\nBest Match:")
print(documents[best_match_index])
