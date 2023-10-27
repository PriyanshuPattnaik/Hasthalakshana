import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from gtts import gTTS
# To install this module, run:
# python -m pip install Pillow
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
import json
import streamlit as st
import tensorflow as tf
from keras.models import load_model
from keras.utils import load_img
from keras.utils import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np
from keras.models import load_model
from gtts import gTTS
import os
import time
from translate import Translator
from data_list import learning_content


st.set_page_config(layout="wide", page_icon="Assets/icon.png")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown( hide_streamlit_style, unsafe_allow_html=True) 

# st.set_page_config(layout="wide", page_icon="Assets/icon.png" )
#st.sidebar.image('images/Azure_Image.png', width=300)
st.sidebar.image("Assets/logo.png", use_column_width=True)
st.sidebar.markdown('You are the same...')


app_mode = st.sidebar.selectbox("Navigation",
                                ["Hasthalakshana", "Learn" , "Image to Text", "Image to Speech", "Speak Your Thoughts"])

# st.write('<style>div.row-widget.stRadio > div{flex-direction:column;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('An idea by students of Vikash Residential School Bhubaneswar| Address')

if app_mode =='Hasthalakshana':
    #st.image('images/wp4498220.jpg', use_column_width=True)
    st.markdown('''
              # Welcome to Hasthalakshana\n 
              ####  Hasthalakshana is an initiative for the people who cannot speak
                ''')
  

if app_mode == 'Learn':
    st.markdown('''
    # Learn Indian Sign Language
    ''')

    selected_section = st.selectbox("Select a section to learn", list(learning_content.keys()))

    for item in learning_content[selected_section]:
        item_name = item["name"]
        video_url = item["video_url"]
        st.button(f"Learn {item_name}", key=f"video_{item_name}")
        st.write(f'<a href="{video_url}" target="_blank">Watch Video</a>', unsafe_allow_html=True)







               

if app_mode=='Image to Text':
  #st.image('sign.jpg'),use_column_width=True )
  st.title("Image to Text")
  st.text("")
 
  
  image_file =  st.file_uploader("Upload Images (less than 1mb)", type=["png","jpg","jpeg"])

  if image_file is not None:
    img = Image.open(image_file)
    st.image(image_file,width=250,caption='Uploaded image')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')#PNG
    image = byte_io.getvalue()

  if image_file is None:
    image_file="data/A/101.jpg"  
    st.text("Demo image")
    img = Image.open(image_file)
    st.image(image_file,width=250,caption='Uploaded image')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')#PNG
    image = byte_io.getvalue()
  
  button_translate=st.button('Click me',help='To give the image')
  
  
  if (button_translate and image_file) or (button_translate and image_file)  :
    class_names= ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    img_height,img_width=180,180
    model = load_model('models/ISLmodel.h5')
    #class_names = model.class_names
    demo_image_path = image_file
    img = tf.keras.utils.load_img(demo_image_path, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    st.text("The hand sign of the above image is : ")
    #st.subheader(class_names[np.argmax(score)])
    word=class_names[np.argmax(score)]

    st.subheader(word)



    
if app_mode=='Image to Speech':
  
  image_file =  st.file_uploader("Upload Images (less than 1mb)", type=["png","jpg","jpeg"])
  if image_file is not None:
    img = Image.open(image_file)
    st.image(image_file,width=250,caption='Uploaded image')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')#PNG
    image = byte_io.getvalue()
  
  if image_file is None:
    image_file="data/1/101.jpg"  
    st.text("Demo image")
    img = Image.open(image_file)
    st.image(image_file,width=250,caption='Uploaded image')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')#PNG
    image = byte_io.getvalue()
  


  button_translate=st.button('Click me',help='To give the image')

  if button_translate and image_file :
    class_names= ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    img_height,img_width=180,180
    model = load_model('models/ISLmodel.h5')
    #class_names = model.class_names
    demo_image_path = image_file
    img = tf.keras.utils.load_img(demo_image_path, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    st.text("The hand sign of the above image is : ")
    #st.subheader(class_names[np.argmax(score)])
    word=class_names[np.argmax(score)]
    sound_file = BytesIO()
    tts = gTTS(word)
    tts.write_to_fp(sound_file)
    st.audio(sound_file)
    
from PIL import ImageOps

if app_mode == 'Speak Your Thoughts':
    st.title("Translate from Text To Image")
    st.text("")
    letter = st.text_input("Enter only a letter not a word ")
    
    button_col1, button_col2 = st.columns(2)
    with button_col1:
        button_speech = st.button('Speak', help='For text to speech')
    with button_col2:
        button_translate = st.button('Generate', help='To give the image')

    out_path = "data/"+letter.upper()+"/101.jpg"
    
    if button_translate and letter:     
           
        image = Image.open(out_path)
        image_with_border = ImageOps.expand(image, border=10, fill='white')
        st.image(image_with_border, caption=letter, width=300, output_format='PNG', use_column_width=False)
        
    elif button_speech:
        sound_file = BytesIO()
        tts = gTTS(letter)
        tts.write_to_fp(sound_file)
        st.audio(sound_file)


if app_mode == 'Speak Your Thoughts':
    st.text("")
    paragraph = st.text_area("Enter a Word or a Paragraph")

    button_col1, button_col2 = st.columns(2)
    with button_col1:
        button_tl = st.button('Speech', help='For text to speech')
    with button_col2:
        button_word = st.button('Enter', help='To give the image')
    if paragraph and button_word:
        words = paragraph.split()
        for word in words:
            with st.expander(f"Word '{word}'"):
                letters = list(word.upper())
                for letter in letters:
                    out_path = f"data/{letter}/101.jpg"  # assuming the image file name is always '101.jpg'
                    try:
                        image = Image.open(out_path)
                        st.image(image, caption=letter, width=300)
                    except:
                        st.error(f"No image found for the letter '{letter}' in the word '{word}'")
        st.text("")
    elif button_tl:
         sound_file = BytesIO()
         tts = gTTS(paragraph)
         tts.write_to_fp(sound_file)
         st.audio(sound_file)


