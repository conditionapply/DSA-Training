# "You have a set of integers s, which originally contains all the numbers from 1 to n.
#  Unfortunately, due to some error, one of the numbers in s got duplicated to another number
# in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form 
# of an array.


# Example 1:
# Input: nums = [1,2,2,4]
# Outpu
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

# Example 2:
# Input: nums = [1,1]
# Output: [1,2]"


def findDM(nums):
    n =len(nums)
    sum_ideal = n*(n+1)//2
    sum_squares_ideals = n*(n+1)*(2*n+1)//6
    sum_actual = sum(nums)
    sum_squares_actual = sum(x*x for x in nums)
    sum_diff = sum_actual-sum_ideal
    sum_squares_diff = sum_squares_actual-sum_squares_ideals
    sum_xy=sum_squares_diff//sum_diff
    x = (sum_diff +sum_xy)//2
    y = x-sum_diff
    return [x,y]
nums=[1,1]
print(findDM(nums))