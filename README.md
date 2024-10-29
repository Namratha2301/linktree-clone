# Simple Linktree clone

> A Streamlit app to store all your personal links, similar to [Linktr.ee](https://linktr.ee/).

# Demo App 
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://linktree-clone-namratha.streamlit.app/)

<img width="744" alt="Screenshot 2024-10-29 at 8 33 12 PM" src="https://github.com/user-attachments/assets/1ab314c9-f53d-4251-a139-7a9b4bf9c830">


[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://linktree-clone-inonzmwvngkdpcfctwbggr.streamlit.app/#gowri-namratha-meedinti-cs-grad)

# Getting Started

Follow these steps to set up your own Streamlit links page:

**Step 1**: [Generate a copy of this repository](https://github.com/Namratha2301/links/generate) and name it anything except `your-username.github.io`.

**Step 2**: Customize your links page by editing the `streamlit_app.py` file:

```python
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://github.com/Namratha2301/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Gowri Namratha Meedinti, CS Grad')
st.info('Cornell CS Grad; Versatile problem solver with a passion for creativity and innovation in data and technology.')

icon_size = 24

# GitHub Button
st_button('github', 'https://github.com/Namratha2301', 'My GitHub', icon_size)

# LinkedIn Button
st_button('linkedin', 'https://www.linkedin.com/in/namrathameedinti', 'Connect on LinkedIn', icon_size)

# Email Button
st_button('email', 'mailto:gm568@cornell.edu', 'Email Me', icon_size)

**Step 3**: Deploy to Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud) and log in to your account.
2. Click on the **New app** button.
3. Select the repository you created in the previous steps.
4. Click on the **Deploy!** button.

After a few moments, your new **links page** should be accessible.



