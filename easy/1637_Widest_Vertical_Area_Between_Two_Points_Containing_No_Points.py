class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted([i[0] for i in points])
        max = 0
        for i in range(len(x)-1):
            candidate = x[i+1] - x[i]
            if  candidate > max:
                max = candidate

        return max