import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config("Central Limit Theorem", layout="wide")
st.header("Visualization of Central Limit Theorem")
st.write("Produced by Prasad Posture")

left, right = st.columns(2)

with left:
	size = int(st.slider("Sample Size",100, 10000, 2000))
	mu = st.slider("Mean",0,10,5)
	sigma = st.slider("Standard Deviation",1,10,5)
	dist_type = st.selectbox('Select Distribution:',('Normal','LogNormal'))
	if dist_type=='Normal':
		population = np.random.normal(mu, sigma, size)
	else:
		population = np.random.lognormal(mu, sigma, size)

with right:
	fig =  px.histogram(population)
	st.plotly_chart(fig)


left1, right1 = st.columns(2)

with left1:
	# Creating the list to store all the means of each sample: 
	samp_no  = st.slider("Number of Means:",10,int(size*0.5),int(size*0.05))
	sample_size = st.slider("Select Sample Size:",10,int(size*0.1),int(size*0.01))
	means = []
# taking 50 samples each time
	for x in range(samp_no): 
    		sample = np.random.choice(population,sample_size)
    		mean = np.mean(sample)
    		means.append(mean)
with right1:
	fig1 =  px.histogram(means)
	st.plotly_chart(fig1)

