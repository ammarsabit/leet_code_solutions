# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        lower_bound  = 1
        upper_bound = n+1

        while lower_bound < upper_bound:
            number = (upper_bound+lower_bound)//2
            guessed = guess(number)
            if guessed == 0:
                return number

            elif guessed == -1:
                upper_bound = number

            else:
                lower_bound = number
        