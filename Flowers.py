# "You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not 
# empty, and an integer n, return true if n new flowers can be planted in the flowerbed without
#  violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n=2


def placeFlowers(flowerbed,n):
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i]==0:
            if (i ==0 or flowerbed[i-1]==0) and (i==length - 1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                count+=1
                if count>=n:
                    return True
                else:
                    return False
flowerbed = [1,0,0,0,1]
n =2
print(placeFlowers(flowerbed,n))