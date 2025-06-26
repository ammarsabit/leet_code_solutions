class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fre = dict()
        for num in nums:
            if num not in fre:
                fre[num] = 1
            else:
                fre[num] += 1

        for n in fre:
            if fre[n] > len(nums)//2:
                return n