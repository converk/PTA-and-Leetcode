#买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices):
        allsum = 0
        while prices != []:
            buy = 0
            for i in range(len(prices)):
                if i != len(prices)-1:
                    if prices[i] < prices[i+1]:
                        buy = i
                        break
                else:
                    buy = i
            sell = buy
            for i in range(buy, len(prices)):
                if i != len(prices)-1:
                    if prices[i+1] < prices[i]:
                        sell = i
                        break
                else:
                    sell = i
            count = prices[sell]-prices[buy]
            allsum = allsum+count
            prices = prices[sell+1:]
        return allsum
        """
        :type prices: List[int]
        :rtype: int
        """
