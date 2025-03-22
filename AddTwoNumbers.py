# You are given two non-empty linked lists representing two non-negative integers. The digits 
#  are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

def AddTwoNumbers(l1,l2):
    result =[]
    carry =0
    for i in range(max(len(l1),len(l2))):
        val1 = l1[i] if i<len(l1) else 0
        val2 =l2[i] if i<len(l1) else 0
        total = val1 +val2+carry
        carry = total//10
        result.append(total%10)
    if carry:
        result.append(carry)
    return result
l1 = [9,9,9]
l2 = [1,5,7]

result = AddTwoNumbers(l1,l2)
print(result)