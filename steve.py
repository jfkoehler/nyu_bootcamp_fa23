import streamlit as st
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = 3*x + 4 + np.random.normal(size = len(x))
df = pd.DataFrame({'x': x, 'y': y})


st.header('Welcome to my app')
st.scatter_chart(df)
