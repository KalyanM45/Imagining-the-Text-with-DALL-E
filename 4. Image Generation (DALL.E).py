import openai
import urllib.request
from PIL import Image
import streamlit as st

openai.api_key = "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"

def generate_image(image_description):
    
    img_response = openai.Image.create(
        prompt = image_description,
        n = 1,
        size = "512x512")
    
    img_url = img_response['data'][0]['url']
    
    urllib.request.urlretrieve(img_url, 'img.png')
    
    img = Image.open("img.png")
    
    return img

st.title("Create your Own Image ")

img_description = st.text_input('Image Description')

if st.button('Generate Image'):
    
    generated_img = generate_image(img_description)
    st.image(generated_img)