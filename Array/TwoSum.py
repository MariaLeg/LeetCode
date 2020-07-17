# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residual = dict()
        for i in range(len(nums)):
            if residual.get(nums[i]) is None:
                residual[target - nums[i]] = i
            else:
                return [i, residual[nums[i]]]

nums = [0, 32, -1]
print(Solution().twoSum(nums, 31))
