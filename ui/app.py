import streamlit as st
import requests
from pathlib import Path

MCP_SERVER_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="🍕 Pizza Ordering App", layout="centered")

# ---------- LOAD EXTERNAL CSS ----------
css_path = Path("ui/styles/style.css")

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='title'>🍕 Pizza Ordering App</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-Ready Pizza Ordering System</div>", unsafe_allow_html=True)

# ---------- MAIN CARD ----------
st.markdown("<div class='main-card'>", unsafe_allow_html=True)

# Fetch menu
menu_response = requests.get(f"{MCP_SERVER_URL}/menu")
menu = menu_response.json()["menu"]

pizza_display_map = {
    f"{item['name']} - ₹{item['price']} (Medium)": item["name"]
    for item in menu
}

st.markdown("<div class='label'>Choose your pizza</div>", unsafe_allow_html=True)
selected_display = st.selectbox("", list(pizza_display_map.keys()))
pizza_name = pizza_display_map[selected_display]

st.markdown("<div class='label'>Choose size</div>", unsafe_allow_html=True)
size = st.radio("", ["Small", "Medium", "Large"], horizontal=True)

if st.button("🍽️ Order Pizza"):
    response = requests.post(
        f"{MCP_SERVER_URL}/order",
        json={"pizza": pizza_name, "size": size}
    )

    data = response.json()

    st.markdown(f"""
    <div class='success-box'>
        <p><b>🎉 Order Placed Successfully!</b></p>
        <p><b>Pizza:</b> {data['pizza']}</p>
        <p><b>Size:</b> {data['size']}</p>
        <p class='price'>💰 Price: ₹{data['price']}</p>
        <p><b>Order ID:</b> {data['order_id']}</p>
        <p><b>ETA:</b> {data['eta']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
