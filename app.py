# This is a project created by Emilio Rogalla

import streamlit as st
import matplotlib.pyplot as plt
from keras.datasets import mnist

st.title('My App')

(trainX, trainy), (testX, testy) = mnist.load_data()

plt.imshow(trainX[0], cmap=pyplot.get_cmp('gray'))

st.pyplot()


