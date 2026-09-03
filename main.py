from gemini_service import get_product_category
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

from recommendation import recommend_product
from compare import compare_products
from recommend import recommend
from checkout import generate_checkout

user_query = input("What do you want to buy? ")

query = get_product_category(user_query)

print(f"\nDetected Category: {query}")

comparison = compare_products(query)

print("\nAvailable Products:\n")

for p in comparison:
    print(
        f"{p['name']} | ₹{p['price']} | Rating: {p['rating']}"
    )
recommended = recommend_product(user_query)

if recommended:
    print("\nRecommended Product:")
    print(recommended["name"])
    print("Price:", recommended["price"])
    print("Rating:", recommended["rating"])

    print("\nReason:")
    print(
        f"{recommended['name']} was selected because "
        f"it has one of the highest ratings within your budget "
        f"and offers good value for a student buyer."
)
else:
    print("\nNo product found within your budget.")
