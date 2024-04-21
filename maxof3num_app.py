import streamlit as st
st.write('find max of 3 given numbers')

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

print("You entered:", number1, number2, number3)

largest_number = max(number1, number2, number3)
print("The largest number is:", largest_number)
