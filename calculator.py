# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:10:51 2021

@author: Code
"""

value1=int(input("Enter first value: "))
value2=int(input("Enter second value: "))
opr=input("chose operation: ")


if opr== "+":
    print(value1+value2)
elif opr== "-":
    print(value1-value2) 
elif opr== "*":
    print(value1*value2)
elif opr=="/":
    print(value1/value2)
else:
    print("invalid opr...")