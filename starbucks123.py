
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Starbucks Coffee App",
    page_icon="☕",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f5f0e8;
}
h1, h2, h3 {
    color: #006241;
}
div.stButton > button {
    background-color: #006241;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}
div.stButton > button:hover {
    background-color: #004c32;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Header
st.title("☕ Starbucks Coffee")
st.subheader("Your favorite coffee, just one click away!")

st.markdown("---")

# Sidebar
st.sidebar.title("☕ Starbucks Menu")
page = st.sidebar.radio(
    "Choose a page",
    ["Home", "Coffee Menu", "My Cart", "About Us"]
)

# Coffee products
products = {
    "Caffè Latte": 450,
    "Cappuccino": 400,
    "Americano": 350,
    "Caramel Macchiato": 550,
    "Mocha": 500,
    "Espresso": 300,
    "Frappuccino": 600,
    "Cold Coffee": 450
}

# Home Page
if page == "Home":
    st.header("Welcome to Starbucks! 💚")

    st.write(
        "Discover your favorite coffee and enjoy "
        "a delicious coffee experience."
    )

    st.markdown("### ☕ Fresh Coffee. Happy Moments.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Coffee Choices", "8+")

    with col2:
        st.metric("Quality", "Premium")

    with col3:
        st.metric("Experience", "Amazing")

    st.markdown("---")
    st.subheader("Our Popular Drinks")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=600",
            use_container_width=True
        )
        st.write("☕ Delicious Coffee")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=600",
            use_container_width=True
        )
        st.write("🥤 Refreshing Drinks")

# Coffee Menu
elif page == "Coffee Menu":
    st.header("☕ Explore Our Coffee Menu")

    st.write("Choose your favorite drink and add it to your cart.")

    cols = st.columns(2)

    for index, (name, price) in enumerate(products.items()):
        with cols[index % 2]:
            with st.container(border=True):
                st.subheader(name)
                st.write(f"Price: Rs. {price}")

                if st.button(
                    f"Add to Cart - {name}",
                    key=f"add_{index}",
                    use_container_width=True
                ):
                    st.session_state.cart.append(
                        {"name": name, "price": price}
                    )
                    st.success(f"{name} added to cart!")

# Cart Page
elif page == "My Cart":
    st.header("🛒 My Shopping Cart")

    if st.session_state.cart:
        total = 0

        for index, item in enumerate(st.session_state.cart):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.write(
                    f"**{item['name']}** - Rs. {item['price']}"
                )

            with col2:
                if st.button("Remove", key=f"remove_{index}"):
                    st.session_state.cart.pop(index)
                    st.rerun()

            total += item["price"]

        st.markdown("---")
        st.subheader(f"Total Amount: Rs. {total}")

        if st.button("Place Order", use_container_width=True):
            st.success("Thank you! Your order has been placed.")
            st.session_state.cart = []
            st.rerun()

    else:
        st.info("Your cart is empty. Please add some coffee!")

# About Us
elif page == "About Us":
    st.header("💚 About Starbucks Coffee")

    st.write("""
    Welcome to our Starbucks-inspired coffee application!

    Our goal is to provide a simple and enjoyable
    experience for coffee lovers.

    Explore our coffee menu, add your favorite drinks
    to your cart, and enjoy a beautiful coffee experience.
    """)

    st.subheader("Our Mission")
    st.write("Making every coffee moment special! ☕")

# Footer
st.markdown("---")
st.caption("© 2026 Starbucks Coffee App | Made with Streamlit ☕")
