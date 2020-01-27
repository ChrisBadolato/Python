import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")

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

def test2Problem2(n):

 primes = [x for x in range(2,n*2) if isPrime(x) & if next(y) == True for y in range(1,n)]
 print(primes)
def next(n):
	if n%2 == 0:
		return True
	else:
		return False

def isPrime(n):

    if (n==1):
     return False
    elif (n==2):
     return True;
    else:
     for x in range(2,n):
      if(n % x==0):
       return False
      return True 

test2Problem2(3)


def test2Problem3a():

    return df['salary'].std()
 
def test2Problem3b():

    df_males = df[df['sex'] == 'Male']
    return def_males['salary'].mean()
	
def test2Problem3c():

    df_females = df[ df['sex'] == 'Female' ]
    df_females_assistant_professors = df[ df['rank'] == 'AsstProf' ]
	
    return df_females_assistant_professors['salary'].max()
	


print(test2Problem3b)