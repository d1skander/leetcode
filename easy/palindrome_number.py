#python3 easy/palindrome_number.py


class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        if self.x < 0:
            return False
        if (-2**31) <= x <= (2**31 - 1):
            str_number = str(self.x)
            if str_number == str_number[::-1]:
                return True
            else:
                return False