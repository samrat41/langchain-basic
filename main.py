import streamlit as st
import langchain_helper

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Italian", "Mexican", "American", "South Indian", "North Indian"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**", response['menu_items'])

