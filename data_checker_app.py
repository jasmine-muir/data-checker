import pandas as pd
import streamlit as st
import os

uploaded_file = st.file_uploader("Choose a file", type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    option = st.selectbox(
    'Crop ID Column Name',
     df.columns )
else:
    print("upload file") 
uploaded_file.seek(0)    
crops = df[option].value_counts(dropna=False)
    #print(crops)
st.bar_chart(crops)
st.map(df)