class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        
        for i in range(len_nums):
            if nums[i] == target:
                return i
        
        pointer = 0
        for i in range(len_nums):
            if nums[i] < target:
                pointer = i + 1
                
        return pointer