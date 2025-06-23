class Solution(object):
    def plusOne(self, digits):

        digits_copy = int(''.join(str(i) for i in digits))
        string_answer = list(str(digits_copy + 1))
        final_answer = [int(i) for i in string_answer]
        return final_answer