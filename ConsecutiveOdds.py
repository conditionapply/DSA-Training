# Given an integer array arr, return true if there are three consecutive odd numbers 
# in the array. Otherwise, return false.
# Example 1:
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.


def three_consecutive_odds(arr):
    count = 0
    for num in arr:
        if num % 2 == 1:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False
arr = [2,6,4,1]

print(three_consecutive_odds(arr))
