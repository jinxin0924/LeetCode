__author__ = 'Xing'
# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given
# prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
# is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
#
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        #用pointer指向primes各个
        pointer=[0]*len(primes)
        L=[1]
        length=1
        while length<n:
            min_number,min_index_list=L[pointer[0]]*primes[0],[0]
            for index in range(1,len(primes)):
                # print(pointer[index],len(L))
                current=L[pointer[index]]*primes[index]
                if current==min_number:
                    min_index_list.append(index)
                elif current<min_number:
                   min_number,min_index_list=current,[index]

            for min_index in min_index_list:
                pointer[min_index]+=1
            L.append(min_number)
            length+=1
        return L[-1]
s=Solution()
print(s.nthSuperUglyNumber(12,[2,7,13,19]))


