# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' 
# or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while 
# the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

# Example 1:
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.

# Example 2:
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.

# Example 3:
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".

# def Half(s):
#     strlist = str(s)
#     count = 0
#     for i in range(len(strlist)):
#         print(i)
#         if i ==0 and strlist[i+1] == 0:
#            count+=1
#         elif (i !=0 and strlist[i+1] != 0):
#            count+=1
#     return count
           



# s = "1111"
# print(Half(s))



def Half(s):
    count = 0
    count2 = 0
    for i in range(len(s)):
        expceted1 = 0 if i %2==0 else "1"
        expected2 =1 if i %2==0 else   "0"
        if s[i]!= expceted1:
            count+=1
        if s[i]!= expected2:
            count2+=1
    return min(count,count2)


s = "1111"
print(Half(s))
