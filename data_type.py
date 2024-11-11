# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 21:58:30 2021

@author: Code
"""


print("Numbers Data type")

print("01-Number data type")
a=10
print(a, type(a)) #type()is used for knowing the value of datatype using 

a=10.11
print(a, type(a)) #type()is used for knowing the value of datatype using 
a=10+3j
print(a, type(a)) #type()is used for knowing the value of datatype using 


#string Data type
print("02-String data type")

b= "Welcome" #''value'' we use double quotation for write a datatype in word
print(b, type(b))
b= '''
    to 
    my coursse ''' #'''value''' we use three quotation for write a datatype in pragraph 
print(b, type(b))

#List Data type
print("03-List data type")

c=[15,'course',3.8] #this list is like a array where '15' is on zero index, 'course'is on one index and '3.8' is on second index
c[1]= "python" # here we change the one index value which shows its mutable datatype
print(c, type(c))


#Tuple Data type
print("04-Tuple data type")
d=(14,13,'python course') #this is act same like list but bcoz it is unmutable so it can't be change anywhere
print(d, type(d))

#Dictionary Data type
print("05-String data type")

e={
      'Course':'python',
      'status':'Learning'
   }
print(e['Course']) #this is to get the specic value
print(e,type(e))


#Set Data type
print("06-Set data type")

f={13,12,14}
print(f,type(f))