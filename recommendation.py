from products import products

def search_product(query):
    result = []

    for product in products:
        if query.lower() in product["name"].lower():
            result.append(product)

    return result