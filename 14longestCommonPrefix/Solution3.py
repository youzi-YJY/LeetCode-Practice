class Solution(object):
    def LongestCommonPrefix(self,s):
        if not s:
            return ""
        s.sort()
        n=len(s)
        a=s[0]
        b=s[n-1]
        res=""
        for i in range(len(a)):
            if i < len(b) and a[i]==b[i]:
                res+=a[i]
            else:
                break
        return res