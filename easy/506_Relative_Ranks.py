class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        relative_rank = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(4, len(score)+1):
            relative_rank.append(str(i))

        nums_dict  = {rank : score for score, rank in enumerate(sorted(score, reverse=True))}

        output = []
        for n in score:
            output.append(relative_rank[nums_dict[n]])

        return output   