import streamlit as st
import math

# Function to compute y
def compute_y(T, N_pub, N_top5, D_assoc, D_full):
    log_y = 12.14 - 0.0104 * T + 0.0053 * N_pub + 0.0206 * N_top5 + 0.2269 * D_assoc + 0.4877 * D_full
    return math.exp(log_y)  # Convert log y to y

# Page Configuration
st.set_page_config(page_title="Compute Projected Salary", page_icon="📈", layout="centered")

st.subheader("This web tool projects the expected salary of Economics professors at colleges across the United States based on a model which accounts for the main determinants of base pay.")

st.text("In our view, these are:")

st.text("1. The number of years since completion of PhD")
st.text("2. The total number of publications across all journals")
st.text("3. The total number of publications in the top 5 Economics journals")
st.text("4. Status as an Associate or Full Professor")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, .stApp {
        background-color: #121212;
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .main-title {
        font-size: 36px;
        text-align: center;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .sub-text {
        font-size: 18px;
        text-align: center;
        font-weight: 300;
        margin-bottom: 20px;
    }
    .stButton button {
        background-color: #1DB954;
        color: black;
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #1ED760;
    }
    .stNumberInput, .stRadio {
        background: #1E1E1E;
        color: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
    }
    .stNumberInput input {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown('<p class="main-title">Compute Projected Salary</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Enter your values below and click Compute.</p>', unsafe_allow_html=True)

# Use containers for better structure
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        T = st.number_input("Number of Years since PhD Completion (T)", value=0.0, format="%.2f")
        N_pub = st.number_input("Total Number of Publications (N_pub)", value=0.0, format="%.2f")

    with col2:
        N_top5 = st.number_input("Number of Publications in Top 5 Journals (N_top5)", value=0.0, format="%.2f")
        D_assoc = st.radio("Are you currently an Associate Professor (1 for Yes)? (D_assoc)", [0, 1])
        D_full = st.radio("Are you currently a Full Professor (1 for Yes)? (D_full)", [0, 1])

# Compute Button
if st.button("🔍 Compute"):
    result = compute_y(T, N_pub, N_top5, D_assoc, D_full)
    st.success(f"✅ Computed y = {result:.4f}")

