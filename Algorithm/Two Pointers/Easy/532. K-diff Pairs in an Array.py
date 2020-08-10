"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].

"""

Solutions:

# Two - pointers:

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # sorted nums
        nums = sorted(nums)
        
        right, left, results, end = 1, 0, 0, len(nums)
        while right < end:
            while right + 1 < end and nums[right] == nums[right+1]:
                right += 1
            while left + 1< right and nums[left] + k < nums[right]:
                left += 1
                
            if nums[left] + k == nums[right]:
                results += 1
            right += 1
        return results
        
# binary search

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        def find_pair(arr, k, i):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if abs(arr[mid] - i) == k:
                    return arr[mid]
                else:
                    if abs(arr[mid] - i) > k:
                        r = mid - 1
                    else:
                        l = mid + 1
            return None
        nums.sort()
        output = []
        for i in range(len(nums)):
            r = find_pair(nums[i+1:], k, nums[i])            
            if r is not None and r not in output:
                output.append(r)
        return len(output)
        
 # hashmap
 
 class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        result = 0
        counter = collections.Counter(nums)
        for i in counter:
            if k > 0 and i + k in counter:
                result += 1
            elif k == 0 and counter[i] > 1:
                result += 1
        return result
