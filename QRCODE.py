import streamlit as st
import qrcode

st.title("QR Code Generator")

text = st.text_input("Enter text/URL")

if st.button("Generate"):
    img = qrcode.make(text)
    img.save("qr.png")
    st.image("qr.png")
