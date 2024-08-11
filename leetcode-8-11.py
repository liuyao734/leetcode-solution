class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)#初始化一个很大的数
        minprice = inf
        maxProfit = 0 #初始化最大利润为零
        for price in prices: #遍历所有价格
            maxProfit = max(price - minprice, maxProfit)
            #如果当前价格price - minprice > 最大利润maxPrifit,则更新威威prince - minprice;否则保持不变
            minprice = min(price, minprice)
            #如果当前价格price < minprice,则更新当前价格为price;否则保持不变;

        return maxProfit
