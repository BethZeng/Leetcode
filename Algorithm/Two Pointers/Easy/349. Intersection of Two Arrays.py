'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

Solutions:

1. Two Pointers

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        result = []
        nums1.sort()
        nums2.sort()
        index1, index2 = 0, 0
        while (index1 < len(nums1) and index2 < len(nums2)):
            if nums1[index1] > nums2[index2]:
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                if not (len(result) and nums1[index1] == result[len(result)-1]):
                    result.append(nums1[index1])
                index1 += 1
                index2 += 1

        return result


2. Hashmap 

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                ans.append(num)
        return list(set(ans)) #remove duplicate
