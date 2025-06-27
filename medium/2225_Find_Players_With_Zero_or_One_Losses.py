class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_count = dict()
        winners = set(match[0] for match in matches)

        no_lose = []
        one_lose = []

        for match in matches:
            looser = match[1]
            if looser not in lose_count:
                lose_count[looser] = 1
            else:
                lose_count[looser] += 1
        
        for player in winners:
            if player not in lose_count:
                no_lose.append(player)
                
        for player in lose_count:
            if lose_count[player] == 1:
                one_lose.append(player)

        top = [sorted(no_lose), sorted(one_lose)]
    
        return top
        