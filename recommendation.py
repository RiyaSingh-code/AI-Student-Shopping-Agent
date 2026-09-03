from compare import compare_products
from utils import extract_budget


def get_product_category(query):
    query = query.lower()

    if "laptop" in query:
        return "laptop"
    elif "phone" in query:
        return "phone"
    elif "headphone" in query:
        return "headphones"

    return query


def recommend_product(query):
    budget = extract_budget(query)

    category = get_product_category(query)

    products = compare_products(query)
    print("Category:", category)
    print("Products:", products)

    if budget:
        products = [
            p for p in products
            if p["price"] <= budget
        ]

    if not products:
        return None

    best_product = max(
        products,
        key=lambda x: x["rating"]
    )

    return best_product
