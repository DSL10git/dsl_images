import streamlit as st
import requests
import random
# streamlit run main.py
# Title
st.markdown("<h1 style='text-align: center;'>DSL images</h1>", unsafe_allow_html=True)

# Search area
search = st.text_input("## Search DSL images", max_chars=100, value="Japan")
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    mystery_button = st.button("My image is ...")
st.markdown("<h6 style='text-align: center;'>Your image will be here!</h6>", unsafe_allow_html=True)
class PixelsAPI:
    def __init__(self, api_key):
            self.api_key = api_key
            self.base_url = "https://api.pexels.com/v1/"
    def search_images(self, query, per_page=10):
        headers = {"Authorization": self.api_key}
        params  = {"query": query, "per_page":per_page}
        response = requests.get(self.base_url+"search", headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return [photo["src"]["original"] for photo in data["photos"]]
        else:
            print("falied to fetch the images, sorry!", response.status_code)
            return []
if mystery_button == True:
    mystery_list = ["Stars", "Great wall of china", "friends", "pumpkin pie", "moon", "Deep sea", "Jelly fish", "school of fish", "shark", "ice cream", "cheese burger", "milkshake", "fries", "chicken nuggets", "gold", "gems", "ruby", "emerald", "diamond"]
    a = random.choice(mystery_list)
    search = a
    st.markdown(f"## My image is {search}")
    api_key = "wa08KmwCPSaMeH3DXyo9Sz5qljuKATj48g8k7kBPqbbFPxN75PxtNnIW"
    pixels_api = PixelsAPI(api_key)

    images_urls = pixels_api.search_images(search, 10)

    col1, col2 =st.columns(2)
    for idx, url in enumerate(images_urls):
        if idx % 2 == 0:
            with col1:
                st.image(f"{url}", caption=f"URL: {url}")
        else:
            with col2:
                st.image(f"{url}", caption=f"URL: {url}")

if __name__ == "__main__":
    api_key = "wa08KmwCPSaMeH3DXyo9Sz5qljuKATj48g8k7kBPqbbFPxN75PxtNnIW"
    pixels_api = PixelsAPI(api_key)

    images_urls = pixels_api.search_images(search, 10)

    col1, col2 =st.columns(2)
    for idx, url in enumerate(images_urls):
        if idx % 2 == 0:
            with col1:
                st.image(f"{url}", caption=f"URL: {url}")
        else:
            with col2:
                st.image(f"{url}", caption=f"URL: {url}")
