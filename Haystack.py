# Input: haystack = ""sadbutsad"", needle = ""sad""
# Output: 0
# Explanation: ""sad"" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = ""leetcode"", needle = ""leeto""
# Output: -1
# Explanation: ""leeto"" did not occur in ""leetcode"", so we return -1."


def code(haystack,needle):
    for i in range(len(haystack)- len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1    

print(code("leetcode","sad"))        