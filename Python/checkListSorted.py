#Our question is to check if the given list/array is sorted or not

def isSorted(a):
    l = len(a)
    if l==0 or l==1:                    #Base case for recusrion
        return True
    if a[0]>a[1]:                       #condition to check
        return False

    smallerList = a[1:]                 #slicing and calling function with smaller list using recursion 
    isSmallerListSorted = isSorted(smallerList)
    
    if isSmallerListSorted:
        return True
    else:
        return False

#main
a = [1,2,3,4,94,5,6]
print(isSorted(a))
    