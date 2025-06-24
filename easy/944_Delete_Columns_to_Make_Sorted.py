class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count_delete = 0
        n = len(strs)
        for i in range(len(strs[0])):
            for j in range(n-1):
                if strs[j][i] > strs[j+1][i]:
                    count_delete += 1
                    break

        return count_delete