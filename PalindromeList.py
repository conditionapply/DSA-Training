# "Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true
# Example 2:

# Input: head = [1,2]
# Output: false"

def isplaindrome(values):
    return values == values[::-1]
print(isplaindrome([1,2,2,1]))
print(isplaindrome([1,2]))