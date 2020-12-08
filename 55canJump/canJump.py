#贪婪算法
class Solution:
    def canJump(self, nums) -> bool:
        max_position=0
        for i,item in enumerate(nums):
            if max_position>=i and i+item>max_position:
                max_position=i+item
        return max_position>=i