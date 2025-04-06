# "Given an unsorted array of integers nums, return the length of the longest continuous 
# increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
# Example 1:
# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are
#  separated by element
# 4.

# Example 2:
# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it
#  must be strictly
# increasing.

def Long(nums):
    if not nums:
        return 0
    length = 1
    maxl=1
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            length +=1
        else:
            length =1
        maxl = max(maxl,length)
    return maxl
nums = [2,2,2,2,2]
print(Long(nums))