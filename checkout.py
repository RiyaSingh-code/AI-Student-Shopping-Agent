import uuid

def generate_checkout(product):
    order_id = str(uuid.uuid4())[:8]

    return {
        "order_id": order_id,
        "product": product["name"],
        "price": product["price"],
        "checkout_url": f"https://student-shop-agent.vercel.app/pay/{order_id}"
    }