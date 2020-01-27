#Christopher Badolato 3064088
#COP 4020 0001
#Python test
#2/28/2019

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

string = "Give a man a program, frustrate him for a day. Teach a man to program, frustrate him for a lifetime"

dataFrame = pd.read_csv("Salaries.csv")


def test2Problem1(string):
 stringTemp = string
 vowels = ('a', 'e', 'i', 'o', 'u')
 for letter in string.lower():
  if letter in vowels:
   stringTemp = stringTemp.replace(letter,"")

 if stringTemp == "":
  return stringTemp
 else:
  return test2Problem1(stringTemp[1:]) + stringTemp[0]

def vowelCheck(c):
    newstr = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            return True        
    return False
    
#helper function for recursion
def rreverse(string1):
    if len(string1) == 0:
        return string1
    else:
        return rreverse(string1[1:]) + string1[0]
    
#helper functions for prime
def is_prime(number):
    if(number == 1):
        return False
    for x in range(2,number):
        if number%x == 0:
            return False
    return True

def prime(n):
    i = 0
    x = 2
    lst = []
    n = n*2
    while i < n:
        if(is_prime(x)):
            lst.append(x)
            i += 1
        x += 1
    return lst

#problem 2
def test2Problem2():
    N = int(input("Enter value for n: "))
    lst = prime(N)
    result = [lst[i] for i in range(len(lst)) if i%2==0]
    print(result)

#problem 3   

def test2Problem3a(dataFrame):
    dataFrame1 = dataFrame.groupby(['sex'])
    dataFrame2 = dataFrame1.agg('mean')
    print(dataFrame2)

def test2Problem3b(dataFrame):
    dataFrame1 = dataFrame.groupby(['sex'])
    dataFrame2 = dataFrame1.agg('max')
    print(dataFrame2)

def test2Problem3c(dataFrame):
    dataFrame1 = dataFrame.groupby(['salary'])
    dataFrame2 = dataFrame1.agg('std')
    print(dataFrame2)
