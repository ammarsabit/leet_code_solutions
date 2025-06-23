class Solution(object):
    def missingNumber(self, nums):
        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i

        expected_sum = 0
        missin_sum = 0
        expected_sum += (len(nums) * (len(nums)+1)) // 2
        missin_sum = sum(nums)
        
        return expected_sum - missin_sum