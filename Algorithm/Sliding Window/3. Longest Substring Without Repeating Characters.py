# Medium
#Given a string, find the length of the longest substring without repeating characters.
'''
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

Solution 1: 
HashTable + Sliding Window
Using a hashtable to remember the last index of every char.  And keep tracking the starting point of a valid substring.

start = max(start, last[s[i]] + 1)

ans = max(ans, i – start + 1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128
        ans, start = 0, 0
        for i, ch in enumerate(s):
            if last[ord(ch)] != -1:
                start = max(start, last[ord(ch)] + 1)
            ans = max(ans, i - start + 1)
            last[ord(ch)] = i
        return ans
      
      
Solution 2:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        length, left, curmax = 0, 0, 0
        for index, char in enumerate(s):
            if char in dic and dic[char] >= left:
                length = max(length, curmax)
                curmax = index - dic[char]
                left = dic[char] + 1
            else:
                curmax += 1
            dic[char] = index
        return max(length, curmax)
 
