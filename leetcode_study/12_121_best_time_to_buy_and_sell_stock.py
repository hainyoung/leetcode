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
# y축을 입력값, x축을 인덱스값으로 해서 그래프를 그려봐라
# 값을 그래프로 나열해서 시각화해보면 대략 어떤 식으로 풀어야 할 지 직관이 생길 것
# index1은 저점을 가리키고 index 4는 고점을 가리킨다
# 여기서는 현재값을 가리키는 포인터가 우측으로 이동하면서 
# 이전 상태의 저점을 기준으로 가격 차이를 계산하고,
# 만약 클 경우 최댓값을 계속 교체해나가는 형태로 O(n)풀이가 가능
# 이처럼 직접 그림으로 나타내는 시각화 작업을 해 보면
# 어려운 문제를 맞닥뜨려도 풀이에 대한 직관이 떠오를 수 있다
# 이와 같은 시각화는 기술 통계학 Descriptive Statistics 이라고 일컬으며
# 통계학에서도 매우 중요한 연구 분야 중 하나이기도 하다
# 다음과 같이 최댓값, 최솟값을 선언
# profit = -sys.maxsize
# min_price = sys.maxsize
# 최댓값이 되어야 할 profit 변수와 최솟값이 되어야 할 min_price 변수의 초깃값은
# 위와 같이 각각 시스템의 가장 작은 값, 가장 큰 값으로 정한다
# 즉, 최댓값 변수는 최솟값으로 최솟값 변수는 최댓값으로 정한다
# 그래야! 어떤 값이 들어오든 바로 교체될 수 있기 때문이다
# 만약 None으로 잡아두게 되면 비교 시 타입 에러, Type Error 가 발생할 수 있기 때문에
# 이처럼 최솟값, 최댓값은 시스템의 최댓값, 최솟값으로 설정하는 것이 편하다
# 다만 이 문제에서는 최대 이익 profit이 나중에 최종 결과로 리턴되는데
# 입력값이 []인 경우, 즉 빈 배열인 경우에는 자칫 -sys.maxsize가 그대로 리턴될 수도 있기 때문에
# profit = 0
# min_price= sys.maxsize
# 이 문제에서는 위와 같이 0으로 설정
# 어차피 최댓값은 0보단느 항상 커야 하기 때문에 이렇게 해도 문제가 없다
# 이후 최저점과 비교해 더 작을 경우 최솟값을 갱신하고, 현재 값과 최솟ㄱ밧의 차이를 계산해
# 만약 더 클 경우 최댓값 profit을 계속 갱신하면서 반복한다
import sys
def maxProfit2(prices: List[int]):
    profit = 0
    min_price = sys.maxsize

    # renew max value and min value
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

# prices = [7, 1, 5, 3, 6, 4]
# loop1
# price = 7
# min = min(sys, 7) => min = 7
# profit = max(0, 7-7) => profit = 0

# loop2
# price = 1
# min = min(7, 1) => min = 1
# profit = max(0, 1-1) = 0

# loop3
# price = 5
# min = min(1, 5) => min = 1
# profit = max(0, 5 - 1) => 4

# loop4
# price = 3
# min = min(1, 3) => min = 1
# profit = max(4, 3 -1) => 4

# loop4
# price = 6
# min = min(1, 6) => min = 1
# profit = max(4, 6 - 1) => profit = 5

# loop5
# price = 4
# min = min(1, 4) => min = 1
# profit = max(5, 4- 1) => profit = 5