# # Loops and Iterations

# ## Break and Continue
# nums=[1,2,3,4,5]
# for num in nums:
#     if num==3:
#         print('Found')
#         break # breaks out of the loop
#     print(num) # prints 1 2 and then Found

# nums=[1,2,3,4,5]
# for num in nums:
#     print(num) # prints 1 2 3 and then Found
#     if num==3:
#         print('Found')
#         break

# nums=[1,2,3,4,5]
# for num in nums:
#     if num==3:
#         print('Found')
#         continue # skips the current iteration of the loop and then moved to new iteration
#     print(num) # prints 1 2 then Found and then 4 5

# nums=[1,2,3,4,5]
# for num in nums:
#     print(num) # prints 1 2 3 then Found and then 4 5
#     if num==3:
#         print('Found')
#         continue

# ## Loop within a loop
# nums=[1,2,3,4,5,6,7,8,9]
# strs='Beluwuga'
# for num in nums:
#     for str in strs:
#         print(num,str)

# ## Looping for a fixed number of times
# for i in range(10):
#     print(i) # prints 0 to 9

# for i in range(1,11):
#     print(i) # prints 1 to 10

# While loop
x=0
while x<10: # keeps executing until the statement is true
    print(x)
    x+=1 # updating is a must else it will become an infinite loop

# Infinite loop
i=0
while True:
    if i==5:
        break # if this statement isn't there , loop will run infinitely, click at the terminal and then ctrl+c to stop it
    print(i)
    i+=1













































































