class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = {heights[i]:names[i] for i in range(len(names))}
        srted_height = reversed(sorted(heights))
        srted_names = []

        for i in srted_height:
            srted_names.append(people[i])


        return srted_names