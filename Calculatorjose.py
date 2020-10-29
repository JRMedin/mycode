#!/usr/bin/env python3
num1= float(input("choose a number."))
num2= float(input("choose a second number."))
num3= input("choose a symbol.(+-*/):") # this line is causing an error because you're converting + into a float
def add(x,y): # perfect
    print (x+y)

def subtract(x,y):
    print (x-y)

def multiply(x,y):
    print(x*y)

def divide(x,y):
    print(x/y)

if num3 == "+": # perfect
        add(num1,num2)

elif num3 == "-":
    subtract(num1,num2)

elif num3 == "*":
    multiply(num1,num2)

elif num3 == "/":
    divide(num1,num2)
# that should do it!
