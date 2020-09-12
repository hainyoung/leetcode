# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.


# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# 1. Brute-Force
# 가장 먼저 접근할 풀이법
# 처음부터 O(n^2)으로 사고파로를 반복하면 마지막에 최대 이익 산출 가능
def maxProfit1(prices: List[int]):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

# prices = [7, 1, 5, 3, 6, 4]
# loop1
# i = 0, price = 7
# j = 0, 1, 2, 3, 4, 5
# j = 0
# mp = max(7 - 7, 0) = 0
# j = 1
# mp = max(1 - 7, 0) = 0
# j = 2 , mp = max(2 - 7, 0) = 0
# ...
# loop2
# i = 1, price = 1
# j = 1, 2, 3, 4, 5
# j = 1, mp = max(1 - 1, 0) = 0
# j = 2, mp = max(5 - 1, 0) = 4
# j = 3, mp = max(3 - 1, 4) = 4
# j = 4, mp = max(6 - 1, 4) = 5
# j = 5, mp = max(4 - 1, 5) = 5

# loop3
# i = 2, price = 5
# j = 2, 3, 4, 5
# j = 2, mp = max(5 - 5, 5) = 5
# j = 3, mp = max(3 - 5, 5) = 5
# j = 4, mp = max(6 - 5, 5) = 5
# j = 5, mp = max(4 - 5, 5) = 5

# loop4
# i = 3, price = 3
# j = 3, 4, 5
# j = 3, mp = (3 - 3, 5) = 5
# j = 4, mp = (6 - 3, 5) = 5
# j = 5, mp = (4 - 3, 5) = 5

# loop5
# i = 4, price = 6
# j = 4, 5
# j = 4, mp = (6 - 6, 5) = 5
# j = 5, mp = (4 - 5, 5) = 5

# max_price = 5
# but,,,
# time limit exceeded

# 2. calculate difference between low-point and current value
