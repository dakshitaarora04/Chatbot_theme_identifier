from sentence_transformers import SentenceTransformer

#this model transforms sentences into numeric vectors(embedding).

def load_embedding_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model
