def climbingStaircase(n, k):
    def backtracking(n, k, subAns, ans):
        if n == 0:
            ans.append(subAns)
        else:
            for i in range(1, k+1):
                if n - i >= 0:
                    # subAns.append(i)
                    backtracking(n - i, k, subAns+[i], ans)
                else:
                    return
                
    ans = []
    backtracking(n, k, [], ans)
    return ans
