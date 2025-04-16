import streamlit as st
import re
st.set_page_config("Password Strength Meter", page_icon="")
st.title("🔒 Password Strength Meter ⏲️")
st.write("Use this simple tool to check the strength of your password this tool is designed to evaluate the security level of a password based on various criteria such as length, complexity, and uniqueness.")

password = st.text_input("Enter a password and we'll tell you how strong 💪🏻 it is: ", type="password")
message = []
score = 0

if password:
    if len(password) >= 8:
        score +=1
    else:
        message.append("❌ Password should be at least 8 characters long")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score +=1        
    else:
        message.append("❌ Password should be contain both uppercase and lowercase letter")
    if re.search(r"\d",password):
        score +=1
    else:
        message.append("❌ Password should contain at least one digit")
    if re.search(r"[!@#$%^&*]",password):
        score +=1          
    else:
        message.append("❌ Password should contain at least one special character [!@#$%^&*]")
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.success("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.success("🔴 Weak Password - Improve it using the suggestions above.")
    if message:
        st.markdown("## Improvement Suggestions")
        for tip in message:
            st.write(tip)       
else:
    st.write("Please enter a password to get started")            