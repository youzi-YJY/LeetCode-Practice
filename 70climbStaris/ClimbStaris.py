#斐波那契数列的应用
'''
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

动态规划
class Solution:
    def fib(self,N):
    if N<=1: return 1
    a,b=0,1
    for _ in range(N-1):
        a,b=b,a+b
    return b

动态规划
class Solution:
    def fib(self,N):
    if N<=1: return 1
    return self.fib(N-1)+self.fib(N-2)

递归
import functools
class Solution:
    @functools.lru_cache(None)
    def fib(self,N):
        if N<=1: return 1
        return self.fib(N-1)+self.fib(N-2)
'''
#时间复杂度O(1)
class Solution:
    def climbStaris(self,n):
        if n==0:
            return 0
        l0,l1=1,2
        while n>1:
            l0,l1=l1,l0+l1
            n-=1
        return l0

#动态规划：dp[i]=dp[i-1]+dp[i-2]
'''
时间复杂度O(n)
class Solution:
    def fib(self,n):
        dp={}
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
'''
if __name__=="__main__":
    S=Solution()
    number=int(input())
    print(S.climbStaris(number))