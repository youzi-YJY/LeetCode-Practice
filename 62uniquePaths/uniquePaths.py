#动态规划的体现
#函数的参数中，m为行数，n为列数。
#创建dp来存储每一步的状态。
#状态转移方程,后面的解依赖前面的，走到i,j处的路径，dp[i][j]=dp[i-1][j]+dp[i][j-1]
#由于只能向下和右进行移动，从而初始值为dp[i][1]=1,dp[1][j]=1
class Solution:
    def uniquePaths(self,m,n):
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]