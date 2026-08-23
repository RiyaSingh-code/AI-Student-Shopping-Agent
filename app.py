from compare import search_product
from recommendation import recommend

query = input("What are you looking for? ")

results = search_product(query)

if results:
    print("\nProducts Found:\n")

    for item in results:
        print(item)

    best = recommend(results)

    print("\nRecommended Product:")
    print(best)

else:
    print("No products found")
    