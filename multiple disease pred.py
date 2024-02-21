import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide')


# loading the saved models

diabetes_model = pickle.load(open('saved_models\diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('saved_models\heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('saved_models\parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Common diseases Prediction'],
                          icons=['activity','heart','person','thermometer'],
                          default_index=3)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input ('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
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


  
    #code for common disease prediction system
if (selected == "Common diseases Prediction"):
        
        #title of page
    st.title("Common disease Prediction")
        #creating colums if not understood form above :/
    col1,col2,col3,col4,col5 = st.columns(5)
        
        #crating buttons for selection
    with col1:
        Symptom1 = st.checkbox('Cold')
        Symptom1_2 = st.checkbox('Fever')
        Symptom1_3 = st.checkbox('Cough')
        Symptom1_4 = st.checkbox('Diarrehea')
        Symptom1_5 = st.checkbox('Vomiting')
        
    with col2:
        Symptom2 = st.checkbox('Stomach Ache')
        Symptom2_1 = st.checkbox('Muscle/bone Pain')
        Symptom2_2 = st.checkbox('High Heart Beats')
        Symptom2_3 = st.checkbox('Bleading/swelling')
        Symptom2_4 = st.checkbox('skin Iritations')
        
    with col3:
        Symptom3 = st.checkbox('Discomfort')
        Symptom3_1 = st.checkbox('Asthama')
        Symptom3_2 = st.checkbox('Restlessness')
        Symptom3_3 = st.checkbox('Dizziness')
        Symptom3_4 = st.checkbox('Chest Pain')
        
    with col4:
        Symptom4 = st.checkbox('Unresponsive/Unconscious/blackouts')
        Symptom4_1 = st.checkbox('Sucidal thoughts')
        Symptom4_2 = st.checkbox('Lungs History')
        Symptom4_3 = st.checkbox('Muscle Change/speech slured')
        Symptom4_4 = st.checkbox('Difficult Urine Passing')

    with col5:
        Symptom5 = st.checkbox('weight Change')
        Symptom5_1 = st.checkbox('Sweating Excessively')
        Symptom5_2 = st.checkbox('hallucinations')
        Symptom5_3 = st.checkbox('chills/tremor/seizers')
        Symptom5_4 = st.checkbox('Mood change')
        
        
    #if conditions after the result button realsed
    symptom_dict = {}            
    if st.button("Common Diseases's Prediction"):
        symptom_dict = {
        (Symptom1, Symptom1_3, Symptom1_5, Symptom2_1, Symptom5_3): "You may have Dengu",
        (Symptom1_2, Symptom5_3, Symptom2_2): "You may have Malaria",
        (Symptom1_2, Symptom2, Symptom2_3,Symptom1_5,Symptom1_4): "You may have Chronic diarrhea",
        (Symptom1,): "You may have cold fever",
        (Symptom1_2, Symptom1_5, Symptom3_3, Symptom3): "You may have Migraine Effect",
        (Symptom4_1, Symptom5_2, Symptom5_3, Symptom5_4,Symptom3): "You may have Depression/Depression Disorder",
        (Symptom1_2, Symptom1_3, Symptom2_1, Symptom5_3,Symptom5_1): "You may have Pneumonia",
        (Symptom1_3, Symptom2_2, Symptom3, Symptom3_1,Symptom3_4): "You may have Heart Diseases/myocardical issues, Go to Heart Diseases Page for Detailed Summary",
        (Symptom3_4, Symptom2_1, Symptom3, Symptom5_1,Symptom3_2): "You may have HyperClorestrolemia",
        (Symptom1_2, Symptom1_3, Symptom1_4, Symptom2_3,Symptom3): "You may have Scar Infection",
        (Symptom1_2, Symptom2, Symptom2_1, Symptom3_1,Symptom5_4,Symptom4_4,Symptom3): "You may have Infected Urinal track Or kidney related Issue",
        (Symptom5_3, Symptom2_1, Symptom3_3, Symptom2_3): "You may have Anemia",
        (Symptom1_2, Symptom1_3, Symptom2_2, Symptom3_1,Symptom3_4,Symptom3,Symptom4_2): "You may have Chronic Lung related Diseases",
        (Symptom1_2, Symptom2_2, Symptom3, Symptom3_2,Symptom4_3,Symptom5_2,Symptom5_4): "You may have Alzheimer's or Dementia",
        (Symptom1_2, Symptom1_5, Symptom3, Symptom3_1,Symptom3_3,Symptom4_3,Symptom5): "You may have hypothyroidism",
        (Symptom2_2, Symptom2_4, Symptom3, Symptom3_2,Symptom3_3,Symptom4,Symptom4_1,Symptom5_2,Symptom5_3): "You may have Anxiety Or Mental disorder like ADHD or Down-syndrome",
        (Symptom1_2, Symptom1_3, Symptom1_4, Symptom2_1,Symptom5_1,Symptom5_2): "You may have Immunity Dificiency syndrome",
        (Symptom1_2, Symptom1_3, Symptom2_2, Symptom1_4,Symptom2_1,Symptom4_1,Symptom5_3,Symptom5_1,Symptom5_4,Symptom5): "You may have HIV/STD/HIV-infection",
        (Symptom1_2, Symptom2_1, Symptom2_4, Symptom3_4,Symptom5_3): "You may have Cellulitis",
        (Symptom1_2, Symptom2, Symptom4, Symptom3_4,Symptom5_1,Symptom1_5): "You may have Dehyadration",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",
        (Symptom1_2, Symptom2, Symptom2_3, Symptom3_4,Symptom1_5): "You may have Chronic diarrhea",

    }
    
    found = False
    for symptoms, disease in symptom_dict.items():
        if all(symptoms):
            dis = disease
            found = True
            break
    
    if not found:
        dis = "Go to the doctor or contact one from below"


            
    st.success(dis)    
st.write("Contact a Doctor- https://www.apollo247.com/specialties")
st.write("Know your Diseases - ")
st.warning('''WARNING - A medical expert, like a doctor, is best able to help you find the information and care you need. 
               This information is medical advice or diagnosis based on prediction from more than 3000+ paitents.
               Still If you Find anything abnormal rather than searching youe Diseases in any domaain, You should Contact a doctor First
               anything non-serious conditions can be helpful from above or anywhere else. Also Doctors Contact is also given above''')