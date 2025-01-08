import streamlit as st
from streamlit import form_submit_button


st.title("Contact me ")

with st.form(key='email_forms'):
     user_email=st.text_input("Enter Your Email_id:")
     user_text=st.text_area("Enter Your Message:")
     button=form_submit_button('Send')
     if button:
         print("true")


st.header("Linkedin")
st.write("[Linked_in](https://www.linkedin.com/in/kushal-k-314024252/)")

st.header("GIT_HUB")
st.write("[GIT](https://github.com/kushalk47)")

st.header("Gmail")
st.write("[gmail](https://kushalkantharaju536@gmail.com)")

app = Flask(__name__)

# Load station data
stations = pd.read_csv("csv2/stations.txt", skiprows=17)


