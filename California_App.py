import numpy as np
import joblib as jb
import streamlit as st

obj= jb.load("california.joblib")
model = obj["model"]
cols= obj["columns"]

#----------------------------------------
st.title("California App")
In=[]
for i in cols:
    v=st.number_input(f"Enter {i} value: ")
    In.append(v)

if st.button("Click"):
    out=model.predict([In])
    st.success(f"The Median House value is :{out}")
