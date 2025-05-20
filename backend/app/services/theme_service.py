from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def identify_themes(texts, n_clusters=5, n_keywords=8):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(X)

    themes = []
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()

    for i in range(n_clusters):
        keywords = [terms[ind] for ind in order_centroids[i, :n_keywords]]
        themes.append((i, keywords))
    return themes, labels
