from sentence_transformers import SentenceTransformer
import numpy as np
from data import documents

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(documents)

# Save locally
np.save("embeddings.npy", embeddings)
np.save("documents.npy", np.array(documents))

print("Embeddings created and stored locally.")
print(f"Shape: {embeddings.shape}")
