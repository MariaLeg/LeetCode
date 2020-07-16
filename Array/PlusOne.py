# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            if digits[i] + 1 < 10:
                digits[i] += 1
                break
            elif i == 0:
                digits[i] = 0
                digits.insert(0, 1)
                break
            else:
                digits[i] = 0
                i -= 1
        return digits


digits = [1,9,9]
print(Solution().plusOne(digits))
