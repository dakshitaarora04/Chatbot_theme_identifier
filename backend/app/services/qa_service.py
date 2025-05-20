from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class QASystem:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.text_chunks = []

    def build_index(self, chunks):
        self.text_chunks = chunks
        embeddings = self.model.encode(chunks, convert_to_numpy=True)
        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def query(self, question, top_k=3):
        if self.index is None or not self.text_chunks:
            return []

        q_emb = self.model.encode([question], convert_to_numpy=True)
        distances, indices = self.index.search(q_emb, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.text_chunks[idx])
        return results
