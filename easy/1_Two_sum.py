class Solution(object):
    def twoSum(self, nums, target):
        complement = dict()
        for i in range(len(nums)):
            com = target - nums[i]
            if nums[i] in complement:
                return [i, complement.get(nums[i])]
            else:
                complement[com] = i