def get_similar_docs(index, query, k=5, score=False):
    if score:
        return index.similarity_search_with_score(query, k=k)
    return index.similarity_search(query, k=k)
