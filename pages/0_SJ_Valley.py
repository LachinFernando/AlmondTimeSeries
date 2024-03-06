import streamlit as st

IMAGE_ADDRESS = "https://databasin2-filestore.s3.amazonaws.com/c2bfe42273484e6e81df2599bb7dc48a/images/preview.png?v=1435683621"

# set the title
st.title("San Joaquin Valley, California")

# set Image
st.image(IMAGE_ADDRESS)