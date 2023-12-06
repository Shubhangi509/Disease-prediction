import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from plyer import notification
import json
from streamlit_lottie import st_lottie

def load_lottie(path: str):
    with open(path,"r") as f:
        return json.load(f)

anim = load_lottie("C:/Users/diksh/Desktop/Hackathon/anim1.json")
covanim = load_lottie("C:/Users/diksh/Desktop/Hackathon/covanim.json")
heartanim = load_lottie("C:/Users/diksh/Desktop/Hackathon/heartanim.json")
sleepanim = load_lottie("C:/Users/diksh/Desktop/Hackathon/sleepanim.json")
diab_anim = load_lottie("C:/Users/diksh/Desktop/Hackathon/diab_anim.json")
# Loading the models
diabetes = pickle.load(open("C:/Users/diksh/Desktop/Hackathon/diabetes.sav", "rb"))
heart_disease = pickle.load(open("C:/Users/diksh/Desktop/Hackathon/Heart_Model.sav", "rb"))
parkinsons_disease = pickle.load(open("C:/Users/diksh/Desktop/Hackathon/parkinson.sav", "rb"))
sleep_model = pickle.load(open("C:/Users/diksh/Desktop/Hackathon/sleep_disorder.sav", "rb"))
covid = pickle.load(open("C:/Users/diksh/Desktop/Hackathon/covid.sav", "rb"))

# Set the background color using custom CSS
st.markdown("""
    <style>
        div[class="block-container.st-emotion-cache-1y4p8pa.ea3mdgi4"] {
            background: green !important;
        }
    </style>
""", unsafe_allow_html=True)

def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

def ChangeInputColour(font_color = 'white', background_color='violet'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('input[type="number"]');
            for (var i = 0; i < elements.length; ++i) {{ 
                
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)


def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Disease Prediction App',
        timeout=10  # Display time in seconds
    )


selected = option_menu(menu_title = "Navigation",
                           options = ["Diabetes Prediction", "Heart Disease Prediction","Sleep Disorder","Parkinsons Disease Prediction","Covid-19 Prediction"],
                           menu_icon="segmented-nav",
                           default_index=0,
                           orientation="horizontal",
                           styles={
                               "container": {"background-color":"#242224","font-size":"15px","width":"100%","overflow":"auto"},
                               "icon":{"color":"grey","font_size":"20px"},
                               "nav-link":{
                                   "font-size":"20px",
                                   "text-align":"left",
                                   "margin":"0px",
                                   "--hover-color":"#51545c",
                                   "width":"150px",
                                   "display": "inline-block"
                                   },
                               
                           "nav-link-selected":{"background-color":"violet"},},)

# Diabetes Prediction Page:
if selected == "Diabetes Prediction":
    ChangeInputColour()
    st_lottie(diab_anim,speed=1,width=450,height=250)
    st.title("Diabetes Prediction using Machine Learning")
    st.text("Please enter the following information for Diabetes Prediction:")
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies")
        SkinThickness = st.number_input("Skin Thickness Value")
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value")
    with col2:
        Glucose = st.number_input("Glucose Level")
        Insulin = st.number_input("Insulin Level")
        Age = st.number_input("Age of the Person")
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value")
        BMI = st.number_input("BMI Value")

    # Code for Prediction
    diabetes_diagnosis = " "
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diabetes_prediction[0] == 0:
            diabetes_diagnosis = "Hurrah! You have no Diabetes."
            send_notification('Disease Prediction Alert', diabetes_diagnosis)
        else:
            diabetes_diagnosis = "Sorry! You have Diabetes."
            send_notification('Disease Prediction Alert', diabetes_diagnosis)
    st.warning(diabetes_diagnosis)
    ChangeButtonColour('Diabetes Test Result', 'white','violet')
    
    
    
# Heart Disease Prediction Page:
if selected == "Heart Disease Prediction":
    ChangeInputColour()
    st_lottie(heartanim,speed=1,width=350,height=250)
    st.title("Heart Disease Prediction using Machine Learning")
    st.text("Please enter the following information for Heart Disease Prediction:")
    
    # Apply custom class for styling
   
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
     # Apply custom class
    with col1:
        age = st.number_input("Age")
        sex = st.number_input("Sex")
        cp = st.number_input("Chest Pain Types")
        trestbps = st.number_input("Resting Blood Pressure")
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")
        restecg = st.number_input("Resting Electrocardiographic Results")
        oldpeak = st.number_input("ST Depression induced by Exercise")
        ca = st.number_input("Major vessels colored by Fluoroscopy")
    # Close the custom class
    with col2:
        chol = st.number_input("Serum Cholesterol in mg/dl")
        thalach = st.number_input("Maximum Heart Rate Achieved")
        exang = st.number_input("Exercise Induced Angina")
        slope = st.number_input("Slope of the peak exercise ST Segment")
        thal = st.number_input("Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect")
        
    # Code for Prediction
    heart_diagnosis = " "
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        if heart_prediction[0] == 0:
            heart_diagnosis = "Hurrah! Your Heart is Good."
            send_notification('Disease Prediction Alert', heart_diagnosis)
        else:
            heart_diagnosis = "Sorry! You have a Heart Problem."
            send_notification('Disease Prediction Alert', heart_diagnosis)
    st.success(heart_diagnosis)
    ChangeButtonColour('Heart Disease Test Result', 'white','violet')
    ChangeInputColour()


if(selected == "Sleep Disorder"):
    st_lottie(sleepanim,speed=1,width=350,height=250)
    #page title
    st.title("Sleep Health Prediction using Machine Learning")



# getting the input data from the user

    col1, col2 = st.columns(2)  
    
    
    
    with col1:
        gender = st.number_input("Female 0,Male 1")
        
    with col2:
        age = st.number_input("Age")
        
    with col1:
        oc = st.number_input("Accountant 0, Doctor 1,Engineer 2, Lawyer 3, Manager 4,Nurse 5,SalesRep 6,Scientist 7,Software Engineer 8,Teacher 9")
        
    with col2:
        duration = st.number_input("Sleep Duration")
        
    with col1:
        quality = st.number_input("Quality of Sleep")
        
    with col2:
        active = st.number_input("Active")
        
    with col1:
        stress = st.number_input("Stress Level")
        
    with col2:
        wt = st.number_input("Normal 0,Overweight 1")   

    with col1:
        heart = st.number_input("Heart Rate")
        
    with col2:
        daily = st.number_input("Daily Steps")
    
        
    
    
    # code for Prediction
    diagnosis = " "
    
    # creating a button for Prediction    
    if st.button("Test Result"):
        prediction = sleep_model.predict([[gender,age,oc,duration,quality,active,stress,wt,heart,daily]])                          
        
        if (prediction[0] == 0):
          diagnosis = "Insomnia"
          send_notification('Disease Prediction Alert', diagnosis)
        elif (prediction[0] == 1):
            diagnosis = "Little Stress maybe, nothing else."
            send_notification('Disease Prediction Alert', diagnosis)
        else:
          diagnosis = "Sleep Apnea"
          send_notification('Disease Prediction Alert', diagnosis)
        
    st.success(diagnosis)
    
#Parkinsons Disease Prediction Page:

if(selected == "Parkinsons Disease Prediction"):
    
    #page title
    st.title("Parkinsons Disease Prediction using Machine Learning")



# getting the input data from the user

    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
        
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
        
    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
        
    with col1:
        RAP = st.text_input("MDVP:RAP")
        
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
        
    with col3:
        DDP = st.text_input("Jitter:DDP")
        
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
        
    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
        
    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")
        
    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")
        
    with col3:
        APQ = st.text_input("MDVP:APQ")
        
    with col4:
        DDA = st.text_input("Shimmer:DDA")
        
    with col5:
        NHR = st.text_input("NHR")
        
    with col1:
        HNR = st.text_input("HNR")
        
    with col2:
        RPDE = st.text_input("RPDE")
        
    with col3:
        DFA = st.text_input("DFA")
        
    with col4:
        spread1 = st.text_input("spread1")
        
    with col5:
        spread2 = st.text_input("spread2")
        
    with col1:
        D2 = st.text_input("D2")
        
    with col2:
        PPE = st.text_input("PPE")
        
    
    
    # code for Prediction
    parkinsons_diagnosis = " "
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_disease.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 0):
          parkinsons_diagnosis = "Hurrah! You don't have Parkinson's Disease."
          send_notification('Disease Prediction Alert', parkinsons_diagnosis)
        else:
          parkinsons_diagnosis = "Sorry! You have Parkinson's Disease."
          send_notification('Disease Prediction Alert', parkinsons_diagnosis)
        
    st.success(parkinsons_diagnosis)  
 

 		
 
if selected == "Covid-19 Prediction":
    st_lottie(covanim,speed=1,width=350,height=250)
    st.title("Covid-19 Prediction using Machine Learning")
    st.text("Please enter the following information for Covid-19 Prediction:")
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Breathing_Problem = st.number_input("Breathing Problem")
        Fever = st.number_input("Fever")
        Dry_Cough = st.number_input("Dry Cough")
        Sore_throat = st.number_input("Sore throat")
        Running_0se = st.number_input("Running 0se")
        Asthma = st.number_input("Asthma")
    with col2:
        Chronic_Lung_Disease = st.number_input("Chronic Lung Disease")
        Headache = st.number_input("Headache")
        Heart_Disease = st.number_input("Heart Disease")
        Diabetes = st.number_input("Diabetes")
        Hyper_Tension = st.number_input("Hyper Tension")
        Fatigue = st.number_input("Fatigue")
        
    with col3:
        Gastrointestinal = st.number_input("Gastrointestinal")
        Abroad_travel = st.number_input("Abroad travel")
        Contact_with_COVID_Patient = st.number_input("Contact with COVID Patient")
        Attended_Large_Gathering = st.number_input("Attended Large Gathering")
        Visited_Public_Exposed_Places = st.number_input("Visited Public Exposed Places")
        Family_working_in_Public_Exposed_Places = st.number_input("Family working in Public Exposed Places")

    # Code for Prediction
    covid_diagnosis = " "
    if st.button("Covid-19 Test Result"):
        covid_prediction = covid.predict([[Breathing_Problem, Fever, Dry_Cough, Sore_throat, Running_0se, Asthma, Chronic_Lung_Disease, Headache, Heart_Disease, Diabetes, Hyper_Tension, Fatigue, Gastrointestinal, Abroad_travel, Contact_with_COVID_Patient, Attended_Large_Gathering, Visited_Public_Exposed_Places,Family_working_in_Public_Exposed_Places]])
        if covid_prediction[0] == 0:
            covid_diagnosis = "Hurrah! You don't have Covid-19."
            send_notification('Disease Prediction Alert', covid_diagnosis)
        else:
            covid_diagnosis = "Sorry! You have Covid-19."
            send_notification('Disease Prediction Alert', covid_diagnosis)
    st.warning(covid_diagnosis)
    ChangeButtonColour('Covid-19 Test Result', 'white','violet')
    ChangeInputColour()