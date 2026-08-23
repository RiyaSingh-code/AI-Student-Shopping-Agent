def compare_products(products):
    print("\nComparing Products:")

    for product in products:
        print(
            f"{product['name']} | ₹{product['price']} | Rating: {product['rating']}"
        )