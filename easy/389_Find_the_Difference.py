class Solution(object):
    def findTheDifference(self, s, t):
        st = s+t
        unique = 0
        for strs in st:
            unique ^= ord(strs)

        return chr(unique)
        