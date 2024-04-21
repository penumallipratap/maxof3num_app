import streamlit as st
st.write('find max of 3 given numbers')

number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")
number3 = st.number_input("Enter the third number: ")

st.write("You entered:", number1, number2, number3)

largest_number = max(number1, number2, number3)
if st.button("(Calculate)"):  # Add a button to trigger calculation on user click
  st.write("(The maximum number among the entered numbers is", largest_number, ")")

#st.write("The largest number is:", largest_number)
