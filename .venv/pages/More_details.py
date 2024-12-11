import streamlit as st
st.set_page_config(layout='wide')
# Layout: Columns for Achievements and Positions & Responsibilities
col5,emp_col,col6 = st.columns([1.5,0.5,1.5])

with col5:
    st.title("Achievements")
    content4 = '''
    - Represented VTU University at the National-Level Inter-University Competition.
    - Founding member of DACS (Data and Code Society).
    - Organized hackathons and coding bootcamps through DACS.
    - Secured prizes in debate competitions.
    - Volunteered at a local NGO to teach programming to children.
    - Participated in inter-college hackathons.
    - Attended IEEE conferences.
    '''
    st.info(content4)

with col6:
    st.title("Positions & Responsibilities")
    content5 = '''
    - **Captain:** Badminton Team
    - **Coordinator:** IEEE International Conference
    - **Founder and Coordinator:** DACS (Data and Code Society)
    '''
    st.info(content5)

# Create a new row below to add the Education section
col7 = st.columns(1)  # Creating a single column for the Education section

with col7[0]:
    st.title("Education")
    content6 = '''
    - **Bachelor of Engineering in Computer Science and Engineering (Data Science)**  
      SJB Institute of Technology (2022 - Present)  
      CGPA: 8.15 (2 years)

    - **Pre-University Course (PUC)**  
      Chaitanya Pre-University College, Bengaluru  
      Percentage: 90%

    - **St. Mary’s Convent 2020,Bengaluru**  
      SSLC Board  
      Percentage: 96.3%
    '''
    st.info(content6)
