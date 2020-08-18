'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Constraints:

haystack and needle consist only of lowercase English characters.Implement strStr()
'''

Solution:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
  
        for i in range(len(haystack) - len(needle) + 1):
            for k, n_letter in enumerate(needle):
                if n_letter != haystack[i + k]:
                    break
            else: return i
        return -1
        
       
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        substr_len = len(needle)
        str_len = len(haystack)
        if substr_len ==0: return 0
        if substr_len <= str_len:
            for i in range(str_len):
                if haystack[i] == needle[0] and str_len - i >= substr_len:
                    for j in range(substr_len):
                        if  i+j >= str_len  or haystack[i+j] != needle[j]:
                            break
                        elif haystack[i+j] == needle[j] and j == substr_len -1:
                            return i
                elif str_len - i < substr_len or i == str_len-1:
                    return -1
        else:
            return -1
