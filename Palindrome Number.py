__author__ = 'JxKing'
# Determine whether an integer is a palindrome. Do this without extra space.

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x<0:
        return False
    num=x
    s=0
    while x!=0:
        p=x%10
        x=x//10
        s=s*10+p
    return num==s

print(isPalindrome(121))
print(isPalindrome(-11))
print(isPalindrome(11))