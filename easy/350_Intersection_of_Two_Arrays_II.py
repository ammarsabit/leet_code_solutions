class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_dict = dict()
        if len(nums1) < len(nums2):
            num, num3 = nums1, nums2 
        else:
            num, num3 = nums2, nums1

        num_freq = {}
        for n in num:
            if n not in num_freq:
                num_freq[n] = 1
            else:
                num_freq[n] += 1
        output = []
        for m in num3:
            if m in num_freq and num_freq[m]>0:
                output.append(m)
                num_freq[m] -= 1
        
        return output

