# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def search(list1,target):
    count = 0
    result= 0
    for i in list1:
        if target ==i:
            return count
        elif (i<target):
            result = count+1
            count+=1
        else:
            count+=1
    return result
        

print(search([1,3,5,6],7))

