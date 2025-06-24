class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(heights[i], names[i]) for i in range(len(names))]
        srted = [i[1] for i in sorted(people, reverse=True)] 
    
        return srted