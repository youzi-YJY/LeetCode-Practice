import math
class Solution:
    def getPermutation(self,n,k):
        nums=[str(i) for i in range(1,n+1)]
        res=""
        n-=1
        while n>-1:
            t=math.factorial(n)
            loc=math.ceil(k/t)-1
            res+=nums[loc]
            nums.pop(loc)
            k%=t
            n-=1
        return res