# -*- coding: utf-8 -*import streamlit as st-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pickle

def load():
    with open('D:/DS+/9.GIT/dev/cardiovascular_diseases/model.pcl', 'rb') as fid:
        return pickle.load(fid)



st.title('Вероятность сердечно-сосудистых заболеваний')

age = st.slider('Укажите ваш возраст', 30, 90, key='age')
weight = st.slider('Укажите ваш вес', 30, 200, key='weight')

cholesterol = st.selectbox('Выберите ваш уровень холестирина:', [1,2,3], key='cholesterol')

st.write('Укажите ваше давление:')
ap_columns = st.columns(2)
ap_lo = ap_columns[0].number_input('Диастолическое давление:', min_value=40,
                                   max_value=200, step=5, key='ap_lo')
ap_hi = ap_columns[1].number_input('Cистолическое давление:', min_value=60,
                                   max_value=250, step=5, key='ap_hi')
if ap_hi < ap_lo:
    st.error('Cистолическое давление должно быть выше диастолического!')
else:
    st.success("Все верно!")

model = load()
y_pr = (model.predict_proba([[age, ap_hi, ap_lo, weight, cholesterol]])[:,1])*100

st.write(f'Вероятность сердечно сосудистых заболеваний: {y_pr}%')
    


