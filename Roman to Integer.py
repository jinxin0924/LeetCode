__author__ = 'JxKing'
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    romanval = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    num=0
    while romanval:
        word=romanval.pop()
        while word==s[:len(word)]:
            num+=val[len(romanval)]
            s=s[len(word):]
    return num

print(romanToInt('MCMLIV'))
print(romanToInt('MCMXC'))