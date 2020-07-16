# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
#SOLUTION FOR ARRAYS THAT ARE SORTED
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_array = list()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
                continue
            elif nums1[i] > nums2[j]:
                j += 1
                continue
            else:
                intersection_array.append(nums1[i])
                i += 1
                j += 1

        return intersection_array

nums1 = [1,1,2,3,4,4,5,6,6,6,7,10,300]
nums2 = [1,3,3,4,4,4,10,25,78,100,200,300]

print(Solution().intersect(nums1, nums2))