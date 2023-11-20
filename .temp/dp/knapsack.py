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
    n = len(weights) # num of items 
    
    dp = [[0] * (W + 1) for i in range(n + 1)] # zero at the first line, stands for nothing choosed

    
    for i in range(n + 1):
        for j in range(W + 1): # j weight so far
            if weights[i - 1] <= j: # capacity still enough 
                dp[i][j] = max(dp[i-1][j], # i th item not choosed, remaining i-1 items value
                               dp[i-1][j - weights[i-1]] + values[i - 1]) # choose i th item 
            else: # capacity not enough for i th item
                dp[i][j] = dp[i-1][j] # do not choose, remains the i - 1 items value 

    return dp[n][W] 


print(knapsack([1, 3, 4, 5],[1, 4, 5, 7], 7))