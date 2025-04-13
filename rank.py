# Given an array of integers arr, replace each element with its rank.

# # The rank represents how large the element is. The rank has the following rules:

# # Rank is an integer starting from 1.
# # The larger the element, the larger the rank. If two elements are equal, their rank must 
# # be the same.
# # Rank should be as small as possible.

# # Example 1:
# # Input: arr = [40,10,20,30]
# # Output: [4,1,2,3]
# # Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 i
# # s the third smallest.
# # Example 2:
# # Input: arr = [100,100,100]
# # Output: [1,1,1]
# # Explanation: Same elements share the same rank.

# # Example 3:
# # Input: arr = [37,12,28,9,100,56,80,5,12]
# # Output: [5,3,4,2,8,6,7,1,3]

def rank(arr):
    sorted_arr = arr[:]
    sorted_arr.sort()
    rank_map = {}
    rank =1
    for num in sorted_arr:
        if num not in rank_map:
            rank_map[num]=rank
            rank+=1
    result = []
    for num in arr:
        result.append(rank_map[num])
    return result
arr = [40,10,20,30]
print(rank(arr))