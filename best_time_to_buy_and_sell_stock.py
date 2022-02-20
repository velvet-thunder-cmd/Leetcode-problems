class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,m,r=0,0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                m=max(m,(prices[r]-prices[l]))
            else:    
                l=r
            r+=1
        return m
