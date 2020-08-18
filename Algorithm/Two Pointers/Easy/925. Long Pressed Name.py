'''
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
The characters of name and typed are lowercase letters.
'''

Solutions:

Two pointers:

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # two pointers to the "name" and "typed" string respectively
        index_n, index_t = 0, 0

        # advance two pointers, until we exhaust one of the strings
        while index_n < len(name) and index_t < len(typed):
            if name[index_n] == typed[index_t]:
                index_n, index_t = index_n+1, index_t+1
            elif index_t >= 1 and typed[index_t] == typed[index_t-1]:
                index_t += 1
            else:
                return False

        # if there is still some characters left *unmatched* in the origin string,
        #   then we don't have a match.
        # e.g.  name = "abc"  typed = "aabb"
        if index_n != len(name):
            return False
        else:
            # In the case that there are some redundant characters left in typed
            # we could still have a match.
            # e.g.  name = "abc"  typed = "abccccc"
            while index_t < len(typed):
                if typed[index_t] != typed[index_t-1]:
                    return False
                index_t += 1

        # both strings have been consumed
        return True
