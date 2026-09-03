from products import products
import re

def compare_products(user_query):

    matching_products = []

    query = user_query.lower()

    budget = None

    numbers = re.findall(r"\d+", query)
    if numbers:
        budget = int(numbers[0])

    for product in products:

        if product["category"].lower() in query:

            if budget is None or product["price"] <= budget:
                matching_products.append(product)

    matching_products.sort(
        key=lambda x: x["rating"],
        reverse=True
    )

    return matching_products
