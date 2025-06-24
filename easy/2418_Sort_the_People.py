class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(heights[i], names[i]) for i in range(len(names))]
        srted = [name for height, name in sorted(people, reverse=True)] 
    
        return srted