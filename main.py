import random
import string
import streamlit as st

#Setting Page Configuration
st.set_page_config(page_title="Pass Generator", layout="wide")

# Logic Building:
def pass_generator (char, dig, sc):
    character = string.ascii_letters

    if dig:
        character += string.digits # numbers (0-9)

    if sc:
        character += string.punctuation  # @, #, !, $

    return " ".join(random.choice(character) for _ in range (char))

st.markdown("""
    <style>
        .stApp {
            background-color : rgb(255, 204, 204) !important;
        }
        .title {
            display : flex;
            justify-content : center;
            color : rgb(111, 30, 81) !important;
            text-transform : uppercase !important;
        }
        .output-div {
            display : flex;
            border : 2px solid red;
        }
        .output-title {
            color : black !important;
        }
        .output-res {
            color : red !important;
            font-style : italic;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.write("<h1 class='title'>🔢 Password Generator</h1>", unsafe_allow_html=True)

len = st.slider("Select range for your Password", min_value=2, max_value=20, value=6)
digit = st.checkbox("Include Digits")
special_Characters = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = pass_generator(len, digit, special_Characters)
    st.write(f"""
    <div class='output-div'>
        <h3 class='output-title'>Your Generated Password : </h3>
        <h3 class='output-res'>{password}</h3>
    </div>
    """, unsafe_allow_html=True)