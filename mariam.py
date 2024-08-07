from ai71 import AI71 
import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from io import BytesIO
from PIL import Image
import base64

AI71_API_KEY = ""
AI71_BASE_URL = "https://api.ai71.ai/v1/"


def generate_analysis_and_health_plan(patient_prompt):
    chat = ChatOpenAI(
    model="tiiuae/falcon-40b-instruct",
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=True,
)

# Simple invocation:
    response = chat.invoke(
        [
            SystemMessage(content="""You are a neurologist with 20+ years of experience in research and practical medical field. 
                          Your job is to read the patient's current condition, health history, age, weight. allergies related to food and medicine, diet/exercise, medications
                          and mental health from the prompt provided by the user. 
And provide the response of analysis in bullet points:
1.Patient Age
2.brief summary about the patient.
3.calculate the probability of getting a brain disease or multiple diseases or conditions related to brain.
4.expected age range of getting brain disease if the patient does not have any brain disease.
5.probability of cancer
6.Treatment Plan
7.Medication Plan
8.Frequent visits to doctors 
9.Diet and Exercise Plan
10.Meditation Recommendation
11.Mental Health Advice and treatment.
12.Risk Status: Normal, Medium, High."""),
            HumanMessage(content="patient_prompt")
            
        ]
    )
    st.write(response.content)
    




        

st.title("Mariam Neuro AI: Hope for Neuro Humans")

st.write('_Proving hope and guidance for neuro humans like a true shadow. Giving them chance to be happy._')
    
image = Image.open("mariamai.png")
   
st.image(image,width=250)

    
st.markdown(
    """
    <style>
    .stApp {
        background-color: #142a4b;
    }
    </style>
    """,
    unsafe_allow_html=True
)   
ai71_key_input = st.sidebar.text_input("Paste your AI71 API Key here:",type="password")
    
AI71_API_KEY = ai71_key_input

st.sidebar.write("Input examples to try")

st.sidebar.write("https://docs.google.com/document/d/1VCd2AA3zdDhYFfUuStQQw9340RUtf1Yi/edit?usp=sharing&rtpof=true&sd=true")

patient_prompt = st.text_area("Enter the patient's information")

button_response = st.button("Generate Analysis and Health Plan")
if button_response:
    if AI71_API_KEY:
        if patient_prompt:
            generate_analysis_and_health_plan(patient_prompt)
        else:
            st.error("Please enter the patient information")
    else:
        st.error("Please enter the correct AI71 API Key")


