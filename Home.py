import streamlit as st

IMAGE_ADDRESS = "https://www.almonds.com/sites/default/files/2020-03/AL4P2096__CRP.jpg"

# title of the web application
st.title("Almond Plants Health Annomaly Detection")

# set an image
st.image(IMAGE_ADDRESS)

# sub heading
st.subheader("Project About...")
st.markdown("- Almond Cultivation")
st.markdown("- NDVI Index")