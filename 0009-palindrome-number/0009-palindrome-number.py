class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        palindrome=string[::-1]
        if(string==palindrome):
            return True
        else:
            return False
        