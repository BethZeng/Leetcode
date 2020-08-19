## hard

'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''

Solution:

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        output = []
        
        for i in range(len(nums)):
            if i-k >= 0 and nums[i-k] == q[0]:
                q.popleft()
            
            while q and q[-1] < nums[i]:
                q.pop()
            
            q.append(nums[i])
            
            if i >= k-1:
                output.append(q[0])
                
        return output
        
 class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) < k:
            return nums
        
        initial_max = max(nums[0:k])
        res = [initial_max]
        
        for i in range(k, len(nums)):
            if nums[i-k] == initial_max:
                initial_max = max(nums[i-k+1: i+1])
            elif nums[i] > initial_max:
                initial_max = nums[i]
            res.append(initial_max)
        return res
            
