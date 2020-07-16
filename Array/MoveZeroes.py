# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''The idea is to move each non-zero number down the list (behind all leading zeros)
        z_index is the index in array of the first zero in current zero cluster
        '''
        z_index = None
        for i in range(len(nums)):
            if z_index is None and nums[i] == 0:
                z_index = i
                continue
            if z_index is not None and nums[i] != 0:
                nums[z_index], nums[i] = nums[i], nums[z_index]
                z_index += 1

#nums = [0, 0, 1, 6, 5, 0, 0, 0, 3, 4, 1, 0, 0, 8]
#nums = [1,0,0]
nums = [3,3,3,0,0]
Solution().moveZeroes(nums)
print(nums)
