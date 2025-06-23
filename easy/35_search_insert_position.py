class Solution(object):
    def searchInsert(self, nums, target):
        lower_bound = 0
        upper_bound = len(nums) - 1

        if target > nums[upper_bound]:
            return upper_bound + 1 
        elif target <= nums[lower_bound]:
            return 0
        else:
            while lower_bound <= upper_bound:
                middle = (lower_bound + upper_bound) // 2

                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    lower_bound = middle+1
                else:
                    upper_bound = middle-1
            return lower_bound
                
            