# Firstly import the packages

import pysd
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
model = pysd.read_xmile('Revised_Goal_Gap.stmx')

# Name the app

st.title('Over 78 Week Wait Goal Gap Model')

# Add Variables to the Smoking Cessation SD Class object

st.subheader('Slide the Slider to Vary The Adjustment Time')
adjustment_time = st.slider("Adjustment Time", 1, 12, 1)

# Run the Model
values = model.run(params={'Adjustment': adjustment_time})

# Export the Simulation Results

df_waiters = values[['> 78 weeks','Closed Long- Wait Pathways']]
st.subheader('Effects of Increasing Effort to Close Long Waiter Pathways')
st.line_chart(df_waiters)