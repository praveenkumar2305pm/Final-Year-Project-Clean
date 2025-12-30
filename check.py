import streamlit as st 
st.title(" Check power of 2")
def powercheck_2(n):
    if n>0 and (n&(n-1))== 0:
        return " the Number is power of 2"
    else:
        return " The number is not power of 2"    
n=st.number_input("Enter a number")
if st.button("Check"):
    result = powercheck_2(int(n))
    st.write(result)
    
