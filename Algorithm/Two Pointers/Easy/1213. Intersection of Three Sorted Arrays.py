'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
'''


Solution:

Three pointers

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """
        利用三指针，当前非最大的指针向前移动，如果三指针指向的元素相等，那么添加到result
        """
        result = []
        index1, index2, index3 = 0, 0, 0
        while index1 < len(arr1) and index2 < len(arr2) and index3 < len(arr3):
            if arr1[index1] == arr2[index2] == arr3[index3]:
                result.append(arr1[index1])
                index1, index2, index3 = index1+1, index2+1, index3+1
                continue
            maxer = max([arr1[index1],arr2[index2], arr3[index3]])
            if arr1[index1] < maxer:
                index1 += 1
            if arr2[index2] < maxer:
                index2 += 1
            if arr3[index3] < maxer:
                index3 += 1
        return result
