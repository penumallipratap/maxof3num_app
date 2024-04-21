import streamlit as st
st.write('find max of 3 given numbers')

number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")
number3 = st.number_input("Enter the third number: ")

st.write("You entered:", number1, number2, number3)

largest_number = max(number1, number2, number3)
if st.button("計算を実行 (Calculate)"):  # Add a button to trigger calculation on user click
  st.write("入力された数字の中で、最大値は", max_number, "です (The maximum number among the entered numbers is", max_number, ")")

#st.write("The largest number is:", largest_number)
