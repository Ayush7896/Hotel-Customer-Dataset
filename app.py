from distutils.sysconfig import customize_compiler
from operator import mod
from pyexpat import model
import pandas as pd
import tensorflow as tf
import pickle
from tensorflow.keras.models import load_model
import streamlit as st
import time

st.set_page_config(page_title="Hotel's Customer Datset",page_icon="")

data_test=pd.read_csv("test_data_evaluation_part2.csv")
mean_avg=45.50284379443429
data_test['Age']=data_test['Age'].fillna(mean_avg)

data_test['TotalRevenue']=data_test['LodgingRevenue'] + data_test['OtherRevenue']

data_test_new=data_test[['Age', 'AverageLeadTime', 'PersonsNights', 'RoomNights', 'TotalRevenue']]

def main():
    st.title("Hotel's Customer Dataset")

    @st.cache

    def main_function(X):
        with open('model_min_max.pkl' , 'rb') as f:
            scaler = pickle.load(f)
        X=scaler.transform(X)
        model=load_model('model_1.hdf5')
        y_predicted=model.predict(X)

        result=list(map(lambda x:1 if x>=0.5 else 0,y_predicted))
        return result

    data_sample=data_test_new.sample(n=1)
    st.dataframe(data_sample)
    if st.button("Click to Predict"):
        with st.spinner('Wait for it...'):
            time.sleep(2)
        prediction=main_function(data_sample)
        
        st.caption("Predicted Value:")
        st.text(prediction)

        if prediction==[0]:
            st.text("Customer will check in..")
        else:
            st.text("Customer will not check in..")

if __name__=='__main__':
        main()