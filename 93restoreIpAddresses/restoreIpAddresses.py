class Solution:
    def restoreIpAddersses(self,s):
        res=[]
        n=len(s)
        def backtrack(index,tmp,flag):
            #回溯停止的条件:如果索引值走到了字符串的长度或标志位为零
            if index == n and flag ==0 :
                res.append(tmp[:-1])
                #返回到主函数
                return
            #另一停止条件：标志位小于零，返回到主函数
            if flag < 0:
                return

            for j in range(index,index+3):
                if j < n:
                    #需要进行回溯
                    if index == j and s[j] == "0":
                        backtrack(j+1,tmp+s[j]+".",flag-1)
                        #此处需要跳出
                        break
                    #需要进行回溯
                    if 0 < int(s[index:j+1])<=255:
                        backtrack(j+1,tmp+s[index:j+1]+".",flag-1)
            #初始化时候,index=0,tmp="",flag的长度为4.
            backtrack(0,"",4)
            return res


