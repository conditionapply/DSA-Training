# "Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in "
# "arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as
# in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# Example 2:
# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]"


def sortArray(arr1,arr2):
    list1 =[]    #Intializing empty list
    for i in arr2:      #Itering the array
        while i in arr1:     #itering the array1 to check i 
            list1.append(i)   # appedning i to list1 if it matches array1
            arr1.remove(i)     # removing the i from arr1
    arr1.sort()                # sorting arr1
    return list1 + arr1        # combing the values to create the answer

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(sortArray(arr1,arr2))
