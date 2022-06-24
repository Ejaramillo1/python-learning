"""
Solving palindrome resursively
First, convert the string to just characters, by stripping out punctuation, 
and converting upper case to lower case

Then
    Base case: a string of lengh 0 or 1 is a palindrome
    Recursive case: 
        If first character matches last character, then is a palindrome
        if middle section is a palindrome
"""

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
            return ans
    
    def isPal (s):
        if len(s) <= 1:
            return True:
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))