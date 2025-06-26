class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        srted = sorted(nums)
        maximum = 0
        for n in range(0, len(srted), 2):
            maximum += srted[n]

        return maximum
