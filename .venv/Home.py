import streamlit as st

# Set page configuration
st.set_page_config(page_title='Kushal Portfolio',layout='wide')

# Layout: Columns for profile image and introduction
col1,empt_col,col2 = st.columns([1.5,0.2,2.0])

with col1:
    st.image(r"https://github.com/kushalk47/Resume/blob/master/photos/image2.jpg ", width=600)

with col2:
    st.title("Kushal Kadur")
    content = '''
    Hi, I am Kushal K, an undergraduate student at SJBIT, pursuing a degree in Computer Science and Data Science. 
    I am proficient in programming languages like Python, C++, and Java, with expertise in machine learning, 
    data analytics, web development, and more.
    '''
    st.info(content)

# Layout: Columns for technical skills and certifications
col3,emp_col, col4 = st.columns([1.5,0.2,2.0])

with col3:
    st.title("Technical Skills")
    content2 = '''
    - **Languages:** C, C++, Java, Python, R
    - **Tools:** VSCode, Eclipse, Jupyter Notebook
    - **Frameworks:** Flask, React
    - **Databases:** MySQL, MongoDB, SQLite3
    - **Version Control:** Git, GitHub
    - **Expertise:** Cybersecurity, Data Science (Machine Learning, Data Analytics, Data Mining)
    '''
    st.info(content2)

with col4:
    st.title("Certifications")
    content3 = '''
    - **Data Analytics:** Udemy
    - **Complete Ethical Hacking and Cybersecurity:** Udemy
    - **Machine Learning:** Coursera
    - **Prompt Engineering:** Udemy
    '''
    st.info(content3)




# Layout: Columns for projects
col7,emp_col,col8 = st.columns([1.5,0.5,1.5])

with col7:
    st.header("Weather Forecast App")
    st.image(r"https://github.com/kushalk47/Resume/blob/master/photos/xy.png", width=300)
    desc = '''This is a Weather Forecast app that predicts the weather for up to 5 days.'''
    st.write(desc)
    st.write("[Source Code](https://github.com/kushalk47)")

    #st.header("")

    st.header("To-Do App")
    st.image(r"https://github.com/kushalk47/Resume/blob/master/photos/1.png  ", width=300)
    desc = '''A simple To-Do application to help avoid distractions.'''
    st.write(desc)
    st.write("[Source Code](https://todoapp47.streamlit.app)")

    st.header("Chatbot (ChatGPT API Key)")
    st.image(r"https://github.com/kushalk47/Resume/blob/master/photos/9.png", width=300)
    desc = '''An intelligent chatbot created using the ChatGPT API key.'''
    st.write(desc)
    st.write("[Source Code](https://github.com/kushalk47)")

with col8:
    st.header("Market Basket Analysis")
    st.image(r"https://github.com/kushalk47/Resume/blob/master/photos/market_basket_analysis.jpg", width=280)
    desc = '''Using the Apriori algorithm and K-Means clustering to analyze frequently bought items and cluster customers into different groups.'''
    st.write(desc)
    st.write("[Source Code](https://github.com/kushalk47)")

    st.header("Data Analytics (Insurance & UPI)")
    st.image(r"https://github.com/kushalk47/Resume/blob/master/photos/15.png", width=300)
    desc = '''Data analytics project using libraries like NumPy, pandas, seaborn, and SQL to analyze insurance and UPI sales data.'''
    st.write(desc)
    st.write("[Source Code](https://github.com/kushalk47)")
