import uuid

def generate_checkout(product):
    return f"https://checkout.example.com/buy?product={product['name'].replace(' ', '%20')}"
