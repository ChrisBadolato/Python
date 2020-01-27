#Christopher Badolato 3064088
#COP 4020 0001
#Python Assignment
#2/24/2019
#Wordsmith will compare our strings as requested and return the number of values on the list after comprehension
#base_builder converts decimal to base 4 using recursion

def word_smith(String1, String2):
 words = String1.split()
     #makes sure our word is greater than 3 letters and is a letter
 greaterThan3List = [x for x in words if len(x) > 3 and x.isalpha()]
     #calls our other functions on the list created above to find final integer count of list.
 beginWithVowel = [x for x in greaterThan3List if vowelCheck(x) == True or stringCheck(x,String2) == True]
 return len(beginWithVowel)

     #function to check if the first letter of our string is a vowel
def vowelCheck(currentWord):
 first = currentWord[0]
 if first in ('a', 'e', 'i', 'o', 'u', 'y'): return True
 else: return False

    #function to check our current word, with the second string for matching characters.
def stringCheck(currentWord, secondString):
 secondStringList = list(secondString)
 wordList = list(currentWord)
 if set(secondStringList) & set(wordList) != set(): return True
 else: return False

    #finds the base 4 of our decimal input value
def base_builder(inputValue):
 quaternary = recursiveFunction(inputValue)
 total = 0
 qValue = quaternary
 while(qValue > 0):
    total = total + qValue%10
    qValue = qValue//10
 return(total,quaternary)

    #recursive function to grab each digit of the integer
def recursiveFunction(inputValue):
 if inputValue == 0: return 0
 else: return(inputValue % 4 + 10 * recursiveFunction(inputValue//4)) 
 
