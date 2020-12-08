class Solution(object):
    def longgestCommonPrefix(self,s):
        if not s:
            return ""
        res=s[0]
        i=1
        while i<len(s):
            while s[i].find(res)!=0:
                res=res[0:len(res)-1]
            i+=1
        return res