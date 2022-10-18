# Conditionals and Booleans
## Basic syntax
# lang=input()
lang='python'
if lang=='python':
    print('Language is python')
elif lang=='c++':
    print('Language is c++')
else:
    print('False')
# general syntax
condition=False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
## Boolean operations (and or not)
user='Admin'
logged_in=True
if user=='Admin' and logged_in:
    print("Access granted")
else:
    print("Access denied")
# or: executed when either of two statements are true
# and: executed when both of two statements are true
# not: just negates the boolean
if not logged_in:
    print("Please log in")
else:
    print("Welcome")
# difference between == and is is
a=[1,2]
b=[1,2]
print(a==b)
print(id(a))
print(id(b))
print(a is b) # two different objects in the memory ; returns true only when their ids are same
a1=[1,2,3,4,5]
b1=a1
print(id(a1))
print(id(b1))
print(a1 is b1) # same objects in memory

# False Values: (evaluate to false)
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, ',(),[]
    # Any empty mapping. For example, {}
























