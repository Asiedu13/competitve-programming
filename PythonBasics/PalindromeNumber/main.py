class Solution(object):
   def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        y = x
    
        while (y > 0):
            rev = (rev * 10) + ( y % 10)
            y = y // 10

        return x == rev 