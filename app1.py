import streamlit as st
import math

# Function to compute y
def compute_y(T, N_pub, N_top5, D_assoc, D_full):
    log_y = 12.14 - 0.0104 * T + 0.0053 * N_pub + 0.0206 * N_top5 + 0.2269 * D_assoc + 0.4877 * D_full
    return round(math.exp(log_y), 2)  # Convert log y to y

# Page Configuration
st.set_page_config(page_title="Compute Projected Salary", page_icon="📈", layout="centered")

st.title("Projecting the Salaries of Economics Professors")
st.subheader("This web tool projects the expected salary of Economics professors at colleges across the United States based on a model which accounts for the main determinants of base pay.")

st.markdown("""
    <style>
    .highlight-text {
        font-size: 18px;
        font-weight: bold;
        color: #1DB954; /* Spotify Green for contrast */
        padding: 5px;
    }
    .list-text {
        font-size: 16px;
        color: white; 
        padding-left: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="highlight-text">In our view, these are:</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">1️⃣ The total number of years since completing your PhD</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">2️⃣ Your total number of publications in academic journals</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">3️⃣ Your total number of publications in the top 5 Economics journals</p>', unsafe_allow_html=True)
st.markdown('<p class="list-text">4️⃣ Your status as an Associate or Full Professor</p>', unsafe_allow_html=True)


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    /* Auto-detects dark or light mode */
    @media (prefers-color-scheme: dark) {
        html, body, .stApp {
            background-color: #121212;
            color: white;
        }
        .main-title { color: #FFD700; }  /* Gold Title in Dark Mode */
        .sub-text { color: #DDDDDD; }  /* Lighter Gray for Readability */
        .stNumberInput label, .stRadio label {
            color: white !important;
            font-weight: 600;
        }
        .stRadio div[role="radiogroup"] label {
            color: white !important;
            font-size: 16px;
            font-weight: bold;
        }
        .stNumberInput, .stRadio {
            background: #1E1E1E;
            color: white;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
        }
        .stButton button {
            background-color: #1DB954;
            color: black;
        }
    }

    @media (prefers-color-scheme: light) {
        html, body, .stApp {
            background-color: white;
            color: black;
        }
        .main-title { color: #1E1E1E; }  /* Dark Title in Light Mode */
        .sub-text { color: #333333; }
        .stNumberInput label, .stRadio label {
            color: black !important;
            font-weight: 600;
        }
        .stRadio div[role="radiogroup"] label {
            color: black !important;
            font-size: 16px;
            font-weight: bold;
        }
        .stNumberInput, .stRadio {
            background: #F0F0F0;
            color: black;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .stButton button {
            background-color: #007BFF;
            color: white;
        }
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
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        filter: brightness(1.1);
    }
    </style>
""", unsafe_allow_html=True)


# Title and Description
st.markdown('<p class="main-title">Compute Projected Salary</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Enter your values below and click Compute.</p>', unsafe_allow_html=True)

# Display the equation
st.markdown('<p class="sub-text">The model is based on the equation below:</p>', unsafe_allow_html=True)
st.latex(r"""
\log y = 12.14 - 0.0104T + 0.0053N_{\text{pub}} + 0.0206N_{\text{top5}} + 0.2269D_{\text{assoc}} + 0.4877D_{\text{full}}
""")

st.subheader("Input each of these values below to determine your projected salary!")

# Use containers for better structure
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        T = st.number_input("Number of Years since PhD Completion (T)", min_value=0, step=1, format="%d")
        N_pub = st.number_input("Number of Publications (N_pub)", min_value=0, step=1, format="%d")
    
    with col2:
        N_top5 = st.number_input("Number of Publications in Top 5 Journals (N_top5)", min_value=0, step=1, format="%d")
        D_assoc = st.radio("Are you an Associate Professor? (D_assoc)", [0, 1])
        D_full = st.radio("Are you a Full Professor? (D_full)", [0, 1])


# Compute Button
if st.button("🔍 Compute Salary"):
    salary = compute_y(T, N_pub, N_top5, D_assoc, D_full)
    st.success(f"💰 Your expected salary is **${salary:,.2f}**")

