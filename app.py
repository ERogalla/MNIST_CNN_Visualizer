# This is a project created by Emilio Rogalla

import streamlit as st
import matplotlib.pyplot as plt
from keras.datasets import mnist

import time
from session_state import get_state


def main():
    st.title('My App')

    val = st.number_input(label = "Selected Image", value = 0, min_value = 0, max_value = 100)
    number = st.empty()
    trainX = loaddataset()



    run = False 
    i = 0

    if st.button("start"):
        run = True
    if st.button("pause"):
        run = False

    while run:
        loadnumber(trainX, i)
        number.pyplot()
        time.sleep(.5)
        i += 1

@st.cache
def loaddataset():
    (trainX, trainy), (testX, testy) = mnist.load_data()
    return trainX

def loadnumber(trainX, i):
    plt.show(300)
    plt.imshow(trainX[i], cmap=plt.get_cmap('gray'))

if __name__ == "__main__":
    main()
