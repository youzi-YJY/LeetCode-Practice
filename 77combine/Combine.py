#-*-coding:utf-8 -*-
#定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合
#回溯算法的典型应用
'''
回溯的判断，如果我们访问完[1,2],接着我们还需要访问[1,3],这就是回溯，套用回溯的模板就可以。
回溯的时候需要传递哪些参数：
1.nums_new 你的数据就是来源于此。
2.curr_res 需要用此来进行状态判断
3.index 控制访问的数据，如果[1,2]结束，不能再访问2这个值，每次回溯index+1就可以访问到3.
'''
class Solution:
    def combine(self,n,k):
        '''
        :param n: the range of number
        :param k: combinations numbers
        :return: final result
        '''
        #首先生成原始数据
        nums=[i for i in range(1,n+1)]
        #定义一个数组来存储后续的数据
        res=[]

        #定义回溯函数
        def backtrack(nums_new,curr_res,index):
            '''
            :param nums_new:原始数据
            :param curr_res: 更新后的数据
            :param index: 位置参数
            :return:
            '''
            #回溯后成功返回的条件：
            if len(curr_res)==k:
                res.append(curr_res[:])
                return

            #若不满足条件，则进行回溯
            for i in range(index,n):
                curr_res.append(nums[i])
                backtrack(nums_new[index:],curr_res,i+1)
                #回溯过一个元素以后，需要将该元素删除，准备添加新的元素。
                curr_res.pop()
            #特殊情况处理
            if k==0 or n==0:
                return res

        #初始化
        backtrack(nums,[],0)
        return res

if __name__=='__main__':
    S=Solution()
    n=int(input())
    k=int(input())
    print(S.combine(n,k))