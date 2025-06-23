class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = x
        z = 0
        while y > 0:
            z = (z*10) + (y%10) 
            y //= 10
        if z == x:
            return True
        return False

        