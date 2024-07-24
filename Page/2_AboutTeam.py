import streamlit as st

st.title(":violet[...]Dev Geniuses")

col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("SAIF")
   st.markdown('Delhi Technological University')
   st.markdown(" ")
   st.markdown(" ")
   st.markdown('Branch-Electrical Engineering')
   st.markdown(":red[AI] Engineer")
   url1 = 'https://www.linkedin.com/in/md-saif-ahmed-51bbb4202/'
   st.markdown(f'''
<a href={url1}><button style="background-color:DodgerBlue;">LinkedIn</button></a>
''',
unsafe_allow_html=True)

with col2:
   st.header("RISHI")
   st.markdown('Delhi Technological University')
   st.markdown(" ")
   st.markdown(" ")
   st.markdown('Branch-Electrical Engineering')
   st.markdown(":red[ML] Engineer")
   url2 = 'https://www.linkedin.com/in/rishi-kumar-673206294/'
   st.markdown(f'''
<a href={url2}><button style="background-color:DodgerBlue;">LinkedIn</button></a>
''',
unsafe_allow_html=True)
   
with col3:
   st.header("APARNA")
   st.markdown('Indira Gandhi Delhi Technological University for Women')
   st.markdown('Branch-Mechanical and Automation')
   st.markdown(":red[3D] Model Design")
   url3 = 'https://www.linkedin.com/in/aparna-jha-65a05025a/'
   st.markdown(f'''
<a href={url3}><button style="background-color:DodgerBlue;">LinkedIn</button></a>
''',
unsafe_allow_html=True)
   
with col4:
   st.header("NEERAJ")
   st.markdown('Delhi Technological University')
   st.markdown(" ")
   st.markdown(" ")
   st.markdown('Branch-Electrical Engineering')
   st.markdown("Website:red[&]Designing")
   url4 = 'https://www.linkedin.com/in/neeraj-yadav-003226254/'
   st.markdown(f'''
<a href={url4}><button style="background-color:DodgerBlue;">LinkedIn</button></a>
''',
unsafe_allow_html=True)