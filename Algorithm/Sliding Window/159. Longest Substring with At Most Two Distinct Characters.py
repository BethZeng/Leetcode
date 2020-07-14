##Medium

"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""


Solution:
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        start = 0
        max_length, cur_length = 0, 0
        dic = {}
        
        for index, char in enumerate(s):
            if char in dic:
                dic[char] = index
                cur_length += 1
            else:
                if len(dic) < 2:
                    cur_length += 1
                else:
                    break_i, breah_ch = float('inf'), ''
                    for key in dic.keys():
                        if dic[key] < break_i:
                            break_i, break_ch = dic[key], key
                    max_length = max(max_length, cur_length)
                    cur_length = index - break_i
                    del dic[break_ch]
                dic[char] = index
        return max(max_length, cur_length)
