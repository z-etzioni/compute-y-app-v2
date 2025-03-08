import streamlit as st
import math

# Function to compute y
def compute_y(T, N_pub, N_top5, D_assoc, D_full):
    log_y = 12.14 - 0.0104 * T + 0.0053 * N_pub + 0.0206 * N_top5 + 0.2269 * D_assoc + 0.4877 * D_full
    return math.exp(log_y)  # Convert log y to y

# Page title and styling
st.set_page_config(page_title="Compute y", page_icon="📊", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #f5f5f5;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Compute y")

st.markdown("### Enter your values below:")

# Create two columns for better alignment
col1, col2 = st.columns(2)

with col1:
    T = st.number_input("Temperature (T):", value=0.0, format="%.2f")
    N_pub = st.number_input("Number of Publications (N_pub):", value=0.0, format="%.2f")

with col2:
    N_top5 = st.number_input("Top 5 Publications (N_top5):", value=0.0, format="%.2f")
    D_assoc = st.radio("Is Associate? (D_assoc)", [0, 1])
    D_full = st.radio("Is Full? (D_full)", [0, 1])

# Compute button with styling
if st.button("🔍 Compute"):
    result = compute_y(T, N_pub, N_top5, D_assoc, D_full)
    st.success(f"✅ Computed y = {result:.4f}")
