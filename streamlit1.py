import streamlit as st
import pandas as pd
import numpy as np
import time as t

##upto Now Only Functions Used
#st.checkbox("yes")
st.title("welcome to Praveen website !!!")
st.markdown("### This is my first Web page")
st.markdown(":star:")
st.latex(r"""(a+b)^2 =a^2+b^2+2ab""")
st.caption("This is belongs to praveen only!:!:")
st.success("congratulations my dear Praveen Kumar.........")
st.error("you have entered wrong message")
st.warning("You need to work Hard More ......")
st.header("Hello Prends bagunnara !!!")
st.chat_input("Enter a Message...")
st.time_input("What is Present time Now:")
User_input=st.text_input("Enter text")
message=("success","failure")
if User_input == ("success"):
    st.balloons()
    st.header("congratulations!!!")
elif User_input=="failure":
    st.warning("Try Again!!!")
elif User_input=="":
    st.warning("Invalid")

st.image("https://imgs.search.brave.com/AkRhoLjdYXWoAiRQ7XajqUenNJL2nAmhB9q1wzrOkvI/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzMxLzkw/LzUxLzMxOTA1MWM0/ZjlmYTYxYWVhMmZk/ZWIwOWIyODIyOGI3/LmpwZw", width=600)

st.image("24.jpg",width=1000) 
    
#Now widgets
#checkbox
c1=st.checkbox("Hello")
c2=st.checkbox("Bye")
if c1:
    st.write("you Selected: Hello")
if c2:
    st.write("You Selected : Bye")

#button
b3=st.text_input("Enter a number")
st.button("Yes_Submit")
st.button("Cancel")
if b3=="1":
    st.write("Submit")
if b3=="2":
    st.write("Cancel")
    
#radio
st.radio("Select Ur fav Subject:",["Physics","English","Python"])

#selectbox
st.selectbox("choose Your course:",["Python","Java","C"])

#multiselectbox
st.multiselect("I like to eat :",["Biriyani","Chicken Tikka","Chicken lolipops","Khaddu ka Keer"])

#selectslider
st.select_slider("How much rating u will give for my page:",["1","3","5","7","9"])

#slider
st.slider("Rate me:",0,30)

#numberinput
st.number_input("pick a number:",0,10)

#dateinput
st.date_input("Today is Bday:")
#Upload file/folder
st.file_uploader("Upload ur file/folder...")


#colorpicker
st.color_picker("Sel a color for me:):")

#spinner
with st.spinner("Just wait a sec"):
    t.sleep(2)

#sider
st.sidebar.title("Welcome")
st.sidebar.text_input("Username/Email Adress")
st.sidebar.text_input("Password")
c1,c2=st.sidebar.columns(2)
with c1:
    submit=st.sidebar.button("Submit")
with c2:
    clear=st.sidebar.button("clear")
    
#data visualization
#barchart
d=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.title("Bar Chart")
st.bar_chart(d)
st.title("Line Chart")
st.line_chart(d)
st.title("Area Chart")
st.area_chart(d)

#areachart
d1=pd.DataFrame(np.random.randn(30,2),columns=["x","y"])
st.area_chart(d1)