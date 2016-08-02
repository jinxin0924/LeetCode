__author__ = 'Xing'
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit,min_price=0,float('inf')
        for price in prices:
            min_price=min(min_price,price)
            profit=max(profit,price-min_price)
        return profit

s=Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 3, 5, 1, 6, 4]))
print(s.maxProfit([3,3,5,0,0,3,1,4]))