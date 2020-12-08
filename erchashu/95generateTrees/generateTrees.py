# -*-coding:utf-8 -*-
'''
使用动态规划的方法：
1.假设G为1到n所能生成的二叉树的个数
2.假设F为以i为根节点所能生成的二叉树的个数 i<=n
从而有G=F1+F2+.......+Fn
但也有F1=G(i-1)*G(n-i)
最终得到G=G(0)*G(n-1)+G(1)*G(n-2)+....+G(n-1)*G(0)
'''

class Solution:
    def generateTrees(self,number):
        #初始化存储变量
        dp=[0]*int(number+1)
        #初始化前两个变量
        dp[0]=1
        dp[1]=1
        #进行DP操作
        for i in range(2,number+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[-1]

if __name__=="__main__":
    S=Solution()
    number=int(input())
    print(S.generateTrees(number))