'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
'''

Solution:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        start, end = 0, len(s)-1
        while start < end:
            while start < end and not s[start].isalnum():
                start +=1
            while start < end and not s[end].isalnum():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            
            start, end = start +1, end-1
        return True
        
        
        
 class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
    
        def recursive(s, left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            return recursive(s, left, right)
    
        s = new
        return recursive(s, 0, len(s)-1)
