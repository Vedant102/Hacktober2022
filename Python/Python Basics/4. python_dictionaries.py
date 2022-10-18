# Dictionary (key:value pair)
student={'name': 'John','age':25,'courses':['Maths','Science','CS']}
print(student['name'])
print(student['age'])
print(student['courses'])
# or
print(student.get('name','Not Found'))
print(student.get('age','Not Found'))
print(student.get('roll no','Not Found')) # the default value of Not Found is None

# adding/updating a key-value pair
student={'name': 'John','age':25,'courses':['Maths','Science','CS']}
student['roll no']='21075133'
student['age']=21
student.update({'name':'Skittle-chan','phone no':'66234-99867'})
print(student)
for key in student:
    print(student.get(key)) # we get only the value of respective key

# deleting a key
del student['age'] # method 1
print(student)
for key in student:
    print(student.get(key)) # we get only the value of respective key
roll_no=student.pop('roll no') # method 2
for key in student:
    print(student.get(key)) # we get only the value of respective key
print(roll_no)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key,value)






















































































