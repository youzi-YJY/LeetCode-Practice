class Solution:
    def findSubstring(self,s,words):
        from collections import Counter
        if not s or not words:
            return []
        one_word=len(words[0])#获取words里面一个单词的长度
        all_len=len(words)*one_word#能组合成单词的长度
        n=len(s)#字符串的长度
        words=Counter(words)#构建words的哈希表
        res=[]
        for i in range(0,n-all_len+1):
            tmp=s[i:i+all_len]#组合成单词的长度
            c_tmp=[]
            #创建截取字符串的哈希表
            for j in range(0,all_len,one_word):
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp)==words:
                res.append(i)
        return res