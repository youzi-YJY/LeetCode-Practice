class Solution(object):
    def generateParentthesis(self,n):
        if n==0:
            return []
        total_l=[]
        total_l.append([None])#0组括号时记为None
        total_l.append(["()"])#1组括号只有一种情况
        for i in range(2,n+1):#开始计算i组括号时候的括号组合
            l=[]
            for j in range(i):#开始遍历p q p+q=i-1 j作为索引
                now_list1=total_l[j]#p=j时的括号组合情况
                now_list2=total_l[i-1-j]#q=(i-1)-j时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1==None:
                            k1=""
                        if k2==None:
                            k2=""
                        e1="("+k1+")"+k2
                        l.append(e1)#把所可能的情况添加到l中
            total_l.append(l)#l这个list就是i组括号的所有情况，添加到total_l中去，继续求解i=i+1的情况
        return total_l[n]