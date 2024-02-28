import streamlit as st 
import pandas as pd

st.title("BlueTide Dashboard")
accounting_df = pd.read_excel("accounting_heads_pnL.xlsx")
head_values = accounting_df['Head'].unique()

with st.sidebar:
    st.header("Utility of Dashboard")
    st.write("With the head value provided by input widget, you can filter out the dataframe with matching head values using the accounting_heads_pnl worksheet.")

head_value = st.selectbox("Select Head Value", head_values)

if st.button("Get Values", type="primary"):
    filtered_df = accounting_df.loc[accounting_df["Head"] == head_value]
    st.dataframe(filtered_df)