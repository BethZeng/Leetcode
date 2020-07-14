##Medium

"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

Solution:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        left, right = 0, len(s1) - 1
        window_s1 = collections.Counter(s1)
        window_s2 = collections.Counter(s2[left:right])
        
        len_s1, len_s2 = len(s1), len(s2)
        while right < len_s2:
            window_s2[s2[right]] += 1
            if window_s2 == window_s1:
                return True
            window_s2[s2[left]] -= 1
            if window_s2[s2[left]] == 0:
                del window_s2[s2[left]]
            left, right = left+1, right +1
        return False
