## 167. Two Sum II - Input array is sorted 
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

There are three solutions: dictionary, two - pointers, and binary search

# dictionary

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1: return False
        # set up initial dictionary
        seen = {}
        for idx, num in enumerate(numbers):
            other = target - num
            # search the value in dictionary
            if other in seen:
                return [seen[other]+1, idx+1]
            else:
                seen[num] = idx
        return []

# two - pointers 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start+1, end + 1]
            if s > target:
                end -= 1
            elif s < target:
                start += 1

        # return the index list 
        return [-1, -1]

# binary search

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1:
            return False
        def binary_search(self,a, val, start_from):
            if len(a) == 0:
                return False

            left = start_from
            right = len(a)-1
            while left <= right:
                mid = (left+right)//2
                mid_value = a[mid]
                if mid_value ==val :
                    return mid

                elif mid_value < val :
                    left = mid+1

                elif mid_value > val :
                    right = mid-1

            return -1
        
        n = numbers
        index1 = 0
        index2 = 1
        for i in range(len(n)):
            look_for = target - n[i]
            start_from = i+1   
            ind = binary_search(self,n,look_for, start_from)
            if ind != -1:
                index1 = i+1
                index2 = ind+1
                return [index1,index2]
