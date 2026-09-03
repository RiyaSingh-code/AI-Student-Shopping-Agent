import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

client = genai.Client(api_key=api_key)


def ask_gemini(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        
        return getattr(response, "text", None)

    except Exception as e:
        print("Gemini Error:", e)
        return None
def get_product_category(user_query):
    prompt = f"""
You are a category classifier.

Choose ONLY ONE category from this list:

laptop
smartphone
headphones
earbuds

User Request:
{user_query}

Rules:
- Return only the category name.
- Return one word only.
- Do not explain.
- Do not give recommendations.
"""

    category = ask_gemini(prompt)

    if category:
        return category.strip().lower()

    return "laptop"
def generate_product_reasoning(query, product):
    prompt = f"""
You are an AI shopping assistant.

User Query:
{query}

Recommended Product:
Name: {product['name']}
Price: ₹{product['price']}
Rating: {product['rating']}

Explain in 2-3 sentences why this product is a good choice for the user.

Keep it concise and student-friendly.
"""

    response = ask_gemini(prompt)

    if response:
        return response

    return (
        f"{product['name']} is a good option because it fits "
        f"the user's needs and has a rating of {product['rating']}."
    )
