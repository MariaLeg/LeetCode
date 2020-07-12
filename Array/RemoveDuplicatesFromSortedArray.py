#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        unique_number_index = 0
        last_unique_number = nums[0]
        for i in range(len(nums)):
            if nums[i] != last_unique_number:
                last_unique_number = nums[i]
                nums[unique_number_index + 1] = last_unique_number
                unique_number_index += 1
        return unique_number_index + 1

nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5]
n = Solution().removeDuplicates(nums)
print(n, '\n', nums)
