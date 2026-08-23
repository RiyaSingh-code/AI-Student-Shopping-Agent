def recommend(products):
    if not products:
        return None

    best = max(products, key=lambda x: x["rating"])
    return best