__author__ = 'JxKing'
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.

def intToRoman( num):
    """
    :type num: int
    :rtype: str
    """
    dict1={}
    dict1[1]='I'
    dict1[5]='V'
    dict1[10]='X'
    dict1[50]='L'
    dict1[100]='C'
    dict1[500]='D'
    dict1[1000]='M'
    dict1[4]='IV'
    dict1[9]='IX'
    dict1[40]='XL'
    dict1[90]='XC'
    dict1[400]='CD'
    dict1[900]='CM'
    list1=[i for i in dict1]
    list1.sort()
    list2=[]
    while list1:
        x=list1.pop()
        while x<=num:
            num-=x
            list2.append(dict1[x])
    return ''.join(list2)

print(intToRoman(1954),' MCMLIV')
print(intToRoman(1990),' MCMXC')
print(intToRoman(76),'I')


def intToRoman(self, num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res