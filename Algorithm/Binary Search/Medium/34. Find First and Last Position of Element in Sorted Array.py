'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

Solution:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left = right = 0
        
        l, r = 0, len(nums) - 1
        
        # finding leftmost
        while l < r:                       
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        
        # early return
        if nums[r] != target:
            return [-1, -1]
        left = r
        
        # finding rightmost
        l, r = 0, len(nums) - 1
        while l < r:                       
            m = r - (r - l) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        
        right = l
        
        return [left, right]
