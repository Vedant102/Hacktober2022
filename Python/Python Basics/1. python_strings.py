# Strings
from tkinter import PIESLICE


greet='Reyna\'s world'
greet="Reyna's world"
greet='"hello brother"'
greet= """Welcome to my World !
Bhamiya"""
print(greet)
# len() gives the length of the string
print(len(greet)) # symbols, spaces and word starting from next line also counted in length
print(greet[0])

# slicing of strings
print(greet[0:7]) # first index is inclusive while second index is exclusive
print(greet[:7]) # starts with 0th index upto 7th index(exclusive)  (same output as above)
print(greet[6:]) # starts with 6th index upto last index
print(greet.lower()) # all characters converted to lower case
print(greet.upper()) # all characters converted to upper case

# some string functions
greeta="Hemlo Lester"
print(greeta.count('Hemlo')) # tells how many times Hemlo appeared
print(greeta.count('e')) # tells how many times e appeared
print(greeta.find('Hemlo')) # tells the starting index of the argument
print(greeta.find('Hello')) # returns -1 if invalid argument passed
new_greeta=greeta.replace('Lester','fake friend') 
print(greeta)
print(new_greeta)

# adding(concatenating strings)
s1="Hello "
s2="fake friend"
s_final=s1+', '+s2
print(s_final)

# formatting strings
msg='{}, {}. Have a seat!'.format(s1,s2)
print(msg)












