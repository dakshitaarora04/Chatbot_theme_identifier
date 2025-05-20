from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

def identify_themes(chunks, max_clusters=5):
    if not chunks:
        return [], []

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(chunks)

    # Set the number of clusters based on number of chunks
    n_clusters = min(max_clusters, len(chunks))

    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(X)

    themes = {}
    for i, label in enumerate(labels):
        if label not in themes:
            themes[label] = []
        themes[label].append(chunks[i])

    return list(themes.values()), labels

