"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Accepted
"""

Solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return None 
        
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        while start <= len(nums)-1:
            nums[start] = 0
            start += 1
        
