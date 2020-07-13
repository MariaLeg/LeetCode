# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

class Solution(object):
    def rotate(self, nums, k):
        start_index = 0
        previous_index = 0
        current_index = None
        erased_value = nums[0]
        length = len(nums)
        k %= length
        for i in range(length):
            current_index = (previous_index + k) % length
            tmp = nums[current_index]
            nums[current_index] = erased_value
            erased_value = tmp
            if current_index == start_index and i != length - 1:
                previous_index = (current_index + 1) % length
                start_index = previous_index
                current_index = (previous_index + k) % length
                erased_value = nums[previous_index]
            else:
                previous_index = current_index


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Solution().rotate(nums, 3)
print(nums)
