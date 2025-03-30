# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only. 

# Example 1:

# Input: s = ""Hello World""
# Output: 5
# Explanation: The last word is ""World"" with length 5.
# Example 2:

# Input: s = ""   fly me   to   the moon  ""
# Output: 4
# Explanation: The last word is ""moon"" with length 4.
# Example 3:

# Input: s = ""luffy is still joyboy""
# Output: 6
# Explanation: The last word is ""joyboy"" with

def LengthOfLastWord(s):
    length = 0
    word_started =False
    i = len(s)-1
    while i>=0:
        # print("1-",s[i])
        if word_started and s[i] == " ":
            # print("1-k",s[i])
            return length
        if s[i] != ' ':
            # print("1--",s[i])
            word_started = True 
            length+=1
        elif word_started:
            # print("1---",s[i])
            break
        i-=1
    return length

print(LengthOfLastWord("luffy is still joyboy"))