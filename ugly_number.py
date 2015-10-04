__author__ = 'Xin'
# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#  For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.

def isUgly(num):
    if num==0:
        return False
    while num % 2==0:
        num=num/2
    while num % 3==0:
        num=num/3
    while num % 5==0:
        num=num/5
    if num==1:
        return True
    else:
        return False

# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note that 1 is typically treated as an ugly number.


def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    L=[1]
    if n==1:
        return 1
    x,y,z=0,0,0
    for i in range(1,n):
        list1=[2*L[x],3*L[y],5*L[z]]
        m=min(list1)
        if m==list1[0]:
            x+=1
        if m==list1[1]:
            y+=1
        if m==list1[2]:
            z+=1
        L.append(m)
    return L[n-1]

print(nthUglyNumber(19))
