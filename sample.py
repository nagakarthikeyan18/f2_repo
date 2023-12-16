# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:50:53 2022

@author: ank
"""


import numpy as np
import pickle
import streamlit as st


# loading the saved models
loaded_model = pickle.load(open('C:/Users/CVR/Downloads/heart_disease_model.sav', 'rb'))



#creating a function for prediction
def heartdisease_prediction(input_data):
    

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'Do not Worry.The Person does not have a Heart Disease'
    else:
      return 'The Person has Heart Disease. Consult doctor as soon as possible'
  
    
  
def main():
    
    #giving a title
    print("Heart Disease Prediction")
    age=int(input('age'))
    sex=int(input('sex'))
    cp=int(input('cp'))
    trestbps=int(input('trestbps'))
    chol=int(input('chol'))
    fbs=int(input('fbs'))
    cp=int(input('cp'))
    restecg=int(input('restecg'))
    thalach=int(input('thalach'))
    exang=int(input('exang'))
    oldpeak=int(input('oldpeak'))
    slope=int(input('slope'))
    ca=int(input('ca'))
    thal=int(input('thal'))
# =============================================================================
#     st.title('Heart Disease Prediction')
#     
#     
#     # getting the input data from the user
#     
#     col1, col2 = st.columns(2)
#     
#     with col1:
#         aage = st.text_input('Age (29 - 77)')
#         age=int(aage)
#         
#     with col2:
#         ssex = st.text_input('Gender (Male : 1, Female : 0)')
#         sex= int(ssex)
#     with col1:
#         ccp = st.text_input('Chest Pain types (0 : typical type 1 angina, 1 : typical type angina, 2 : non-angina pain, 3 : asymptomatic)')
#         cp=int(ccp)
#     with col2:
#         ttrestbps = st.text_input('Resting Blood Pressure (94 - 200)')
#         trestbps=int(ttrestbps)
#     with col1:
#         cchol = st.text_input('Serum Cholestoral in mg/dl (126 - 564)')
#         chol=int(cchol)
#     with col2:
#         ffbs = st.text_input('Fasting Blood Sugar (value 1 : > 120 mg/dl, value 0 : < 120 mg/dl)')
#         fbs=int(ffbs)
#     with col1:
#         rrestecg = st.text_input('Resting Electrocardiographic results (0 - 2)')
#         restecg=int(rrestecg)
#     with col2:
#         tthalach = st.text_input('Maximum Heart Rate achieved (71 - 202)')
#         thalach=int(tthalach )
#     with col1:
#         eexang = st.text_input('Exercise Induced Angina (Yes : 1, No : 0)')
#         exang=int(eexang)
#     with col2:
#         ooldpeak = st.text_input('ST depression induced by exercise (0 - 6.2)')
#         oldpeak=int(ooldpeak)
#     with col1:
#         sslope = st.text_input('Slope of the peak exercise ST segment (0 - 1)')
#         slope=int(sslope)
#     with col2:
#         cca = st.text_input('Major vessels colored by flourosopy (0 - 3)')
#         ca=int(cca)
#     with col1:
#         tthal = st.text_input('thal (0 : normal, 1 : fixed defect, 2 : reversable defect)')
#         thal=int(tthal )
#        # convert input values to numeric format
# =============================================================================

 




        
    
        #codes for Prdiction
    diagnosis = ''
        
        #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heartdisease_prediction([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal])
            
            
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
