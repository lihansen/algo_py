def n_queens(n):

    def dfs(queens, xy_diff, xy_sum): # queens: queens indices, 
        p = len(queens) # p is the total num of queens in current board 

        if p == n:
            res.append(queens[:])
            return 
        
        for q in range(n): # 1 2 3 4
            if q not in queens:
                if p - q not in xy_diff: # p - q is the xy_diff 
                    if p + q not in xy_sum: # p + q 
                        dfs(queens + [q], xy_diff+ [p-q], xy_sum + [p + q])

    
    res = []
    dfs([], [], [])

    return [ [ "." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in res]

res = n_queens(4)

for sol in res:
    for row in sol:
        print(row)
    print()