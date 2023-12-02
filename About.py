from PIL import Image
import requests

import streamlit as st
from streamlit_lottie import st_lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


import streamlit as st
  
    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open ("images about/family.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.title("About My Family")
    st.write("This is my family picture way back when I graduated at Senior High School")
    st.write("I'm the youngest among two sibling and I have a half sister")
    st.write(
        "My family motivates me to become successful, they are my reason  why I keep pushing everyday.")
    st.write("I want to spoil them, give the things they truly deserve without minding the prize. I want them to see happy and have fun because all their lives they been working so hard to provide our needs and sometimes our wants.")
    st.write("My mothers name is Emelita J. Guerra.")
    st.write("My fathers name is Roberto C. Guerra.")
    st.write("My brother name is Christian J. Guerra.")

    import streamlit as st
  
    # --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open ("images about/brother (2).jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.title("My older brother")
    st.write("He motivates me to strive harder in life.His been an incredible source of strength and I'm endlessly grateful for everything he do.")
    st.write("His resilience,determination and the way he handles challenges head-on inspire me everyday.")
