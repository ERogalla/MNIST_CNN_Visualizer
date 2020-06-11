# This is a project created by Emilio Rogalla

import streamlit as st
import matplotlib.pyplot as plt
from keras.datasets import mnist

import time


def main():
    st.title('My App')

    (trainX, trainy), (testX, testy) = mnist.load_data()

    number = st.empty()
    for i in range(9):
        shownumber(trainX, i)
        number.pyplot()
        time.sleep(1)

def shownumber(trainX, i):
    plt.show(300)
    plt.imshow(trainX[i], cmap=plt.get_cmap('gray'))

if __name__ == "__main__":
    main()
