# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
#SOLUTION FOR ARRAYS THAT ARE NOT SORTED
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''intersection dictionary will have pairs in a format:
        "number from Array-1": [how many times this number appears in Array-1, how many times this number appears in Array-2]
        '''
        intersection = dict()
        #Go through Array-1 and record all the numbers and their occurences
        for number in nums1:
            if intersection.get(number, None) == None:
                intersection[number] = [1,0]
            else:
                intersection[number][0] += 1
        #Go through Array-2 and if the number from Array-2 was also present in Array-1 then count the occurences
        for number in nums2:
            if intersection.get(number, None) is not None:
                intersection[number][1] += 1

        #The result is the numbers that have non-zero occurences in both Arrays and the intersection is
        # the min(occurences in Array-1, occurences in Array-2)
        return [key for key, value in intersection.items() if value[1] != 0 for j in range(min(value))]

nums1 = [1,8,3,10,1,4,12,4,3]
nums2 = [12,3,3,1,4]

print(Solution().intersect(nums1, nums2))