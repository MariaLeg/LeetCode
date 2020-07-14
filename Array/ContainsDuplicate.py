# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False

nums = [1,2,3,4,5,6,7,8]
print(Solution().containsDuplicate(nums))