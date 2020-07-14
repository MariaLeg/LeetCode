from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)[0]

nums = [1,2,4,1,89,2,4]
print(Solution().singleNumber(nums))