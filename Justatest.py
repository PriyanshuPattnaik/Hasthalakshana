import streamlit as st
import googletrans
from googletrans import Translator
import speech_recognition as sr

def transcribe(audio_input,src_lang,tgt_lang):
    try:
        speech = sr.Recognizer()

        with sr.AudioFile(audio_input) as source:
            text = speech.listen(source)
            text_output = speech.recognize_google(text,language=src_lang)  # By default, it converts the speech into english
            translater = Translator()
            out = translater.translate(text_output, dest=tgt_lang)
            text_output=out.text
            return text_output

    except FileNotFoundError:
        return ('Audio file not found')
    except AttributeError as e:
        return (str(e))
    except ValueError as e:
        return (str(e))
    except Exception as e:
        return (str(e))

# Set page title and icon
st.set_page_config(page_title="Speech to Text Translator", page_icon=":microphone:")

# Display app title and description
st.title("Speech to Text Translator")
st.write("Use this app to transcribe your speech into text and translate it into another language.")

# Set default input values
default_src_lang = 'en-US'
default_tgt_lang = 'es'

# Create input fields for audio file and languages
audio_input = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
src_lang = st.text_input("Source language", default_src_lang)
tgt_lang = st.text_input("Target language", default_tgt_lang)

# Create button to trigger transcription and translation
if st.button("Transcribe and Translate"):
    # Check if audio file is uploaded
    if audio_input is None:
        st.warning("Please upload an audio file.")
    else:
        # Call the transcribe function to get the output text
        text_output = transcribe(audio_input, src_lang, tgt_lang)
        # Display the output text
        st.write(text_output)
