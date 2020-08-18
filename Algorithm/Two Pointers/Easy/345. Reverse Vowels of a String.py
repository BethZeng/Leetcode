'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

Solution:

class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 0:
            return s
        
        s_l = list(s)
        start, end = 0, len(s)-1
        while start < end:
            if s_l[start] in 'aeiouAEIOU' and s_l[end] in 'aeiouAEIOU':
                s_l[start], s_l[end] = s_l[end], s_l[start]
                start, end = start+1, end-1
            elif s_l[start] in 'aeiouAEIOU':
                end -= 1
            elif s_l[end] in 'aeiouAEIOU':
                start += 1
            else:
                start, end = start+1, end-1
                
        return "".join(s_l)
