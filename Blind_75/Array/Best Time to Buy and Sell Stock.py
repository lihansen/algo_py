def maxProfit(prices: list[int]) -> int:
    minprice = float("inf")
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit


input = [7,1,5,3,6,4]
res = maxProfit(input)
print(res)