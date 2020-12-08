class Solution(object):
    def maxArea(self,height):
        i,j,res=0,len(height)-1,0
        while i<j:
            if height[i]<height[j]:
                res=max(res,height[i]*(j-i))
                i+=1
            else:
                res=max(res,height[j]*(j-i))
                j-=1
        return res

S=Solution()
height=[1,8,6,2,5,4,8,3,7]
print(S.maxArea(height))