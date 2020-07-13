## Minimum Window Substring (Hard)

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

Solution:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, counts, remain, ans = 0, collections.Counter(t), len(t), None
        for right in range(len(s)):
            curr = s[right]
            if curr in counts.keys():
                if counts[curr] > 0:
                    remain -= 1
                counts[curr] -= 1
                if remain == 0:
                    while left < right:
                        while s[left] not in counts.keys():
                            left += 1
                        counts[s[left]] += 1
                        if counts[s[left]] > 0:
                            counts[s[left]] -= 1
                            break
                        else:
                            left += 1
                    if not ans or len(ans) > right - left:
                        ans = s[left:right+1]
        return ans if ans else ''
