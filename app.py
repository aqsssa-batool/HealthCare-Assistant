from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os  
load_dotenv()
client=Groq(api_key=os.environ["GROQAPIKEY"]) 
MODEL = "openai/gpt-oss-120b"

SYSTEM =( "You are **MediCare AI**, an intelligent, friendly, reliable, and safety-focused healthcare information assistant."
"Your purpose is to help users understand health conditions, diseases, symptoms, medical terminology, prevention methods," 
"and available treatment options in simple language."
"You must provide clear, structured, educational healthcare information about:"

"1. Diseases and medical conditions."
"2. Signs and symptoms of diseases."
"3. Possible causes and risk factors."
"4. Precautions and prevention methods."
"5. Treatment options and medical management."
"6. Medical terminology with proper definitions."
"7. Diagnostic tests and their purposes."
"8. Medicines, their general uses, and common side effects."
"9. Healthy lifestyle practices."
"10. When to consult a doctor or seek emergency medical care.")

st.title("HealthCare Assistant")
st.caption("Ask me anything about healthcare!")
if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"system","content":SYSTEM}]

for m in st.session_state.messages:
    if m["role"]!="system":
        with st.chat_message(m["role"]):
            st.write(m["content"])


user_text=st.chat_input("Type your message...")
if user_text:
    st.session_state.messages.append({"role":"user","content":user_text})
    with st.chat_message("user"): # creates the bubble(box)
        st.write(user_text)

        response= client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages,
            max_tokens=1000
        )

        reply=response.choices[0].message.content

        st.session_state.messages.append({"role":"assistant","content":reply})
        with st.chat_message("assistant"):
            st.write(reply)

