# lists and tuples are useful in working with sequential data
# sets are unordered collections of value with no duplicates
##########################################################################################
# Lists

courses=['history','maths','physics','computer programming']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1]) # always gets us the value of the last element in the list
print(courses[0:3]) # or courses[:3]
print(courses[2:]) # starts from index 2
## adding an element
courses.append('biology')
courses.append('chemistry')
print(courses)
## insert an element
courses.insert(0,'arts') # (index,value of the element)
courses_2=['physical education','humanities']
courses.insert(1,courses_2) # list in list
print(courses)
## inserting multiple elements
courses=['history','maths','physics','computer programming']
courses.extend(courses_2) # adds the element in the list courses_2 to the list courses at the end
print(courses)
## removing an element
courses=['history','maths','physics','computer programming']
courses.remove('history')
print(courses)
popd=courses.pop() # by default removes the last element, and the removed element can also be stored in an variable and be printed
print(popd)
## arranging a list
courses=['history','maths','physics','computer programming']
courses.reverse()
print(courses) # simply reverses the list
## sorting a list
courses=['history','maths','physics','computer programming']
courses.sort() # strings are sorted alphabetically
nums=[1,22,4,66,1,96]
nums.sort() # numbers are sorted in ascending order
print(courses)
print(nums)
courses=['history','maths','physics','computer programming']
courses.sort(reverse=True) # sorts in reverse alphabetical order
print(courses)
courses=['history','maths','physics','computer programming']
sorted_courses=sorted(courses) # in sorted() function the original list is not altered
print(sorted_courses)
## some functions of a list
nums=[1,22,4,66,1,96]
courses=['history','maths','physics','computer programming']
print(min(nums)) # return min element of the list
print(max(nums)) # return max element of the list
print(sum(nums)) # returns sum of elements of the list
print(courses.index('computer programming')) # returns the index of the passed value
print('art' in courses) # returns True if the statement is true else returns False
## loops in a list
courses=['history','maths','physics','computer programming']
for i in courses:
    print(i)
for index,i in enumerate(courses):
    print(index,i)
for index,i in enumerate(courses,start=1):
    print(index,i)
## converting list to string
courses=['history','maths','physics','computer programming']
cou_str1=' - '.join(courses)
cou_str2=' ,'.join(courses)
print(cou_str1)
print(cou_str2)
## converting string to a list
new_list1=cou_str1.split(' - ') # splits (parses) the string at '<space>-<space>' and makes a list of remaning string
new_list2=cou_str2.split(' , ') # splits (parses) the string at '<space>,<space>' and makes a list of remaning string
print(new_list1)
print(new_list2)
## copying of lists
l1=['q','w','e','r','t']
l2=l1
l1[0]='asdfghjk'
print(l2) # any change done in l1 is reflected in l2

#########################################################################################
# Tuples (immutable i.e. can't be modified unlike lists)
tuple1=(3,1,6,2,3,0)
# tuples can be looped through, and accessed by single, else very boring data set

#########################################################################################
# Set (unordered, no duplicate)
set1={1,3,2,2,3,3,4,5,6,3,1,4,5,6,}
print(set1)
c1={'Maths','Chemistry','Physics','Computer Science'}
c2={'Computer Science','Maths','Logistics'}
union_set=c1.union(c2)
intersection_set=c1.intersection(c2)
difference_set=c1.difference(c2)
print(union_set)
print(intersection_set)
print(difference_set)

#########################################################################################























