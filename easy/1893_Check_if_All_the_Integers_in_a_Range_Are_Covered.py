class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            covered=False
            for j in ranges:
                if j[0] <= i <= j[1]:
                    covered=True
                    break
            if covered==False:
                return covered
                
        return covered