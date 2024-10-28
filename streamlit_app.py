import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Gowri Namratha Meedinti, CS Grad')

st.info('Cornell CS Grad; Versatile problem solver with a passion for creativity and innovation in data and technology.”')


# Define the icon size
icon_size = 24  # adjust the icon size as needed

# GitHub Button
st_button('github', 'https://github.com/Namratha2301', 'My GitHub', icon_size)

# LinkedIn Button
st_button('linkedin', 'https://www.linkedin.com/in/namrathameedinti', 'Connect on LinkedIn', icon_size)

# Email Button
st_button('email', 'mailto:gm568@cornell.edu', 'Email Me', icon_size)

# # Portfolio Website Button (Coming Soon)
# st_button('', '#', 'Website Coming Soon', icon_size)
