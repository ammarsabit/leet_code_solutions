class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srted = sorted(nums)
        less=[0]*len(nums)

        unique = {}
        for i, n in enumerate(srted):
            if n not in unique:
                unique[n] = i

        for i in range(len(nums)):
            less[i] = unique[nums[i]]

        return less