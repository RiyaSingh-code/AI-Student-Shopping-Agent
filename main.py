from fastapi import FastAPI
from pydantic import BaseModel

from gemini_service import ask_gemini

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI Student Shopping Agent is running!"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    response = ask_gemini(request.message)

    return {
        "response": response
    }

from recommendation import search_product
from compare import compare_products
from recommend import recommend
from checkout import generate_checkout

query = input("What do you want to buy? ")

products = search_product(query)

compare_products(products)

best_product = recommend(products)

print("\nRecommended Product:")
print(f"Name: {best_product['name']}")
print(f"Price: ₹{best_product['price']}")
print(f"Rating: {best_product['rating']}")

checkout = generate_checkout(best_product)

print("\nCheckout Details:")
print(f"Order ID: {checkout['order_id']}")
print(f"Product: {checkout['product']}")
print(f"Price: ₹{checkout['price']}")
print(f"Checkout URL: {checkout['checkout_url']}")
