# Medium
"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""

NOTE:
Hashmap is also used in this problem. 

Iterate the array and calculate the sum, 

if map[sum-k] in the hashmap, update the maxlength=max(maxlength, i-map[sum-k]).

Note that the map should be initialized as {0:-1} which promises the situation that the first n elements meet the requirement not ignored.

Solution:
 
 class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0 
        max_l, sum_ = 0, 0
        dic = {0:-1}
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ - k in dic:
                max_l = max(max_l, i - dic[sum_-k])
            if sum_ not in dic:
                dic[sum_] = i
        return max_l
