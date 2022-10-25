# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:08:56 2022

@author: Tareq
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu




heart_model=pickle.load(open('C:/Users/Tareq/Desktop/ml2/saved models1/heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/Tareq/Desktop/ml2/saved models1/parkinsons_model.sav','rb'))

Breast_model=pickle.load(open('C:/Users/Tareq/Desktop/ml2/saved models1/Breast_model.sav','rb'))







#side bar for navigations

selected = option_menu(
    menu_title=None,
    options=['Heart Disease prediction',
                           'Parkinsons Prediction',
                           'Breast cancer prediction'
                           ],
    icons=['heart','person','diamond'],
    default_index=0,
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "red", "font-size": "18px"},
                "nav-link": {
                    "font-size": "19px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )
    

 










         
        
     
    
    
    #heart disease predicton page
if(selected=='Heart Disease prediction'):

      #page title
    st.title('Heart Disease prediction using machine learnig')
        
      
      
    col1,col2,col3= st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.selectbox('Sex',["male","female"],index=0)
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl(chol)')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar(fbs)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(restecg)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved(thalach)')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina(exang)')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise(oldpeak)')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy(ca)')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
        
      # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
      
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
if(selected=='Parkinsons Prediction'):

     #page title
    st.title('Parkinsons Prediction using machine learnig')
     
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Breast cancer prediction page
if(selected=='Breast cancer prediction'):

    #page title
    st.title('Breast cancer prediction using machine learnig')
    
    
    #getting the input data from user
    #colum for input fields
    
    col1,col2,col3= st.columns(3)
    
    with col1:
       mean_radius = st.text_input('mean_radius')
        
    with col2:
       mean_texture = st.text_input('mean_texture')
        
    with col3:
        mean_perimeter = st.text_input('mean_perimeter value')
        
        
    with col1:
       mean_area = st.text_input('mean_area')
    
    with col2:
     mean_smoothness = st.text_input('mean_smoothness')
        
    
        
        
    
    
    #code for prediction
    
    Breast_diagnosis= ''
    
    #creating button for predictions
    
    if st.button('Breast cancer Test Results'):
        Breast_prediction= Breast_model.predict([[ mean_radius,mean_texture ,  mean_perimeter, mean_area,mean_smoothness]])
        if( Breast_prediction[0]==0):
            Breast_diagnosis=' The person do not have breast cancer'
        else:
            Breast_diagnosis='The person has breast cancer'
            
    st.success(Breast_diagnosis)  







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    