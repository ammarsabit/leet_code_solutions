class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        fre = dict()
        for n in arr1:
            if n not in fre:
                fre[n] = 1
            else:
                fre[n] += 1
                
        relative_sort = []

        for m in arr2:
            for i in range(fre[m]):
                relative_sort.append(m)
                arr1.remove(m)
        for n in sorted(arr1):
            relative_sort.append(n)

        return relative_sort
        