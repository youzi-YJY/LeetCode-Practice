'''
#Python内建模块
import itertools
def permute(nums):
    return list(itertools.permutations(nums))

#回溯一
class Solution:
    def permute(self,nums):
        res=[]
        def backtrack(nums,tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],tmp+[nums[i]])
            backtrack(nums,[])
            return res'''

#回溯二 深度遍历优先
class Solution:
    def permute(self,nums):
        def dfs(nums,size,depth,path,used,res):
            '''
            :param nums: 原始数组
            :param size: 数组大小
            :param depth: 表示当前递归到第几层
            :param path: 是栈，往下走一层时候，path变量在尾部追加，往回走时候撤销上一次的选择，也是在尾部操作。
            :param used: 初始化为false表示这些数还没有被选择，选定后数组对应位置设为true。
            :param res:存储结果.
            '''
            if depth==size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])

                    dfs(nums,size,depth+1,path,used,res)
                    used[i]=False
                    path.pop()

        size=len(nums)
        if size==0:
            return []
        used=[False for _ in range(size)]
        res=[]
        dfs(nums,size,0,[],used,res)
        return res

if __name__=='__main__':
    nums=[1,2,3]
    solution=Solution()
    res=solution.permute(nums)
    print(res)
'''
布尔数组在这里是判断某个位置上的元素是否已经使用过，有两种等价的替换方式:
哈希表
位掩码，使用一个整数表示布尔数组，可以将空间复杂度降到O(1)，不包括path变量和res变量和递归栈空间的消耗。
#回溯三

class Solution:
    def permute(self,nums):
        def dfs(nums,size,depth,hash_set,path,res):
            if depth==size:
                res.append(path[:])
                return
            for i in range(size):
                if not nums[i] in hash_set:
                    hash_set.add(nums[i])
                    path.append(nums[i])
                    dfs(nums,size,depth+1,hash_set,path,res)
                    path.pop()
                    hash_set.remove(nums[i])
                    
        size=len(nums)
        if size==0:
            return []
        res=[]
        path=[]
        hash_set=set()
        dfs(nums,size,0,hash_set,path,res)
        return res
        
        
permuteUnique II
from typing import List
class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:

                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue

                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

'''