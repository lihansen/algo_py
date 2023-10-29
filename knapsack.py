'''
Statement: 
Given a set of n items numbered from 1 up to n, 
each with a weight wi and a value vi, 
along with a maximum weight capacity W, 
maximize the sum of the values of the items in the knapsack 
so that the sum of the weights is less than or equal to 
the knapsack's capacity.

1, 2, 3 ... n
w1, w2, w3 ... wn
v1, v2, v3 ... vn

capacity W

maximize the value V

'''


def knapsack(weights, values, W):
    nv = len(weights)
    
    dp = [[0] * (W + 1) for i in range(nv + 1)]


    dp [0][0] = 0

    for i in range(nv + 1):
        for j in range(W + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + values[i - 1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[nv][W]


print(knapsack([1, 3, 4, 5],[1, 4, 5, 7], 7))