class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distnict_sort = sorted(set(nums))
        if len(distnict_sort) < 3:
            return distnict_sort[len(distnict_sort)-1]
        else:
            return distnict_sort[len(distnict_sort)-3]