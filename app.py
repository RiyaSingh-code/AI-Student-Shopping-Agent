import streamlit as st
from compare import compare_products
from recommendation import recommend_product
from gemini_service import generate_product_reasoning
import pandas as pd
import random

if "searched" not in st.session_state:
    st.session_state.searched = False

if "checkout" not in st.session_state:
    st.session_state.checkout = False

st.set_page_config(
    page_title="AI Student Shopping Agent",
    page_icon="🛒"
)

# Header
st.title("🛒 AI Student Shopping Agent")

st.markdown("""
### 🎓 Smart Shopping for Students

Find the best products within your budget using AI-powered recommendations.

✅ Budget-based filtering  
✅ Product comparison  
✅ AI reasoning  
✅ Checkout simulation  
""")

# Search Box
query = st.text_input(
    "What would you like to buy?"
)

# Search Button
if st.button("Find Products"):
    st.session_state.searched = True

if st.session_state.searched:

    if query:

        # Get matching products
        products = compare_products(query)

        # Product Count
        st.info(f"Found {len(products)} matching products")
        df = pd.DataFrame(products)

        st.subheader("📊 Product Comparison")

        st.table(
            df[["name", "price", "rating"]]
)

        # Available Products Section
        st.subheader("Available Products")

        if products:

            for p in products:

                st.image(p["image"], width=250)

                st.markdown(f"### {p['name']}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Price", f"₹{p['price']}")

                with col2:
                    st.metric("Rating", p["rating"])


                st.divider()

        else:
            st.warning("No matching products found.")

        # Recommendation
        recommended = recommend_product(query)

        if recommended:

            st.subheader("🎓 AI Student Agent Recommendation")

            st.success(
                f"""
            🏆 Best Choice for Students

            **{recommended['name']}**

            💰 Price: ₹{recommended['price']}

            ⭐ Rating: {recommended['rating']}
            """
            )

            ai_reason = generate_product_reasoning(
                query,
                recommended
            )

            st.info(ai_reason)

            # Checkout Button
            # Checkout Button
            if st.button("Proceed to Checkout"):
                st.session_state.checkout = True


            if st.session_state.checkout:

                st.subheader("🛒 Checkout")

                customer_name = st.text_input("Full Name")

                address = st.text_area("Delivery Address")

                payment_method = st.selectbox(
                    "Payment Method",
                    ["UPI", "Credit Card", "Debit Card", "Cash on Delivery"]
                )

                if st.button("Place Order"):

                    order_id = f"SHOP{random.randint(10000,99999)}"

                    st.balloons()

                    st.success("🎉 Order Placed Successfully!")
                    st.balloons()

                    st.markdown("## ✅ Thank You For Your Order!")

                    st.markdown(
                    f"""
                    ### Order Details

                    **Order ID:** {order_id}

                    **Product:** {recommended['name']}

                    **Delivery:** 3–5 Days

                    **Payment Method:** {payment_method}
                    """
                    )

                    st.info(
                        f"""
            📦 Order Summary

            Order ID: {order_id}

            Customer: {customer_name}

            Product: {recommended['name']}

            Price: ₹{recommended['price']}

            Payment Method: {payment_method}

            Estimated Delivery: 3-5 days
            """
        )
