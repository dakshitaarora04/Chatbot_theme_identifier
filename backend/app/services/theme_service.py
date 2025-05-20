from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

#similar text are grouped as chunks from documents into themes using unsupervised machine learning
#Each chunk of text is converted into a TF-IDF vector (a numerical representation that reflects word importance)
#Now the text converts into a format that a machine learning algorithm can understand.


def identify_themes(chunks, max_clusters=5):
    if not chunks:
        return [], []
        
#K-Means clustering is applied to group similar vectors
    
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(chunks)

    n_clusters = min(max_clusters, len(chunks))

    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(X)

    themes = {}
    for i, label in enumerate(labels):
        if label not in themes:
            themes[label] = []
        themes[label].append(chunks[i])

    return list(themes.values()), labels


