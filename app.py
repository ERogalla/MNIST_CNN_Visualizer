# This is a project created by Emilio Rogalla

import streamlit as st
import matplotlib.pyplot as plt
from keras.datasets import mnist

import time

import SessionState



def main():

    st.title('My App')

    val = st.number_input(label = "Selected Image", value = 0, min_value = 0, max_value = 100)
    number = st.empty()
    trainX = loaddataset()


    print("state is " + str(s.run))

    if st.button("start"):
        s.run = True
        print("started")
    if st.button("pause"):
        s.run = False
        print("paused")

    while s.run:
        s.i += 1
        time.sleep(.5)
        loadnumber(trainX)
        number.pyplot()
        

    loadnumber(trainX)
    number.pyplot()

@st.cache
def loaddataset():
    (trainX, trainy), (testX, testy) = mnist.load_data()
    return trainX

def loadnumber(trainX):
    plt.show(block=False)
    plt.imshow(trainX[s.i], cmap=plt.get_cmap('gray'))

if __name__ == "__main__":
    main()
