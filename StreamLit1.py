import streamlit as st
import pandas as pd

st.title("Police incidents reports from 2018 to 2020")

df=pd.read_csv("Policev1.csv")
df