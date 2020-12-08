'''
class Solution(object):
    def findLongestcommonstr(self, strs):
        res=""
        for tmp in zip(*strs):
            tmp_set=set(tmp)
            if len(tmp_set)==1:
                res+=tmp[0]
            else:
                break
        return res'''


def CheckPermutation(s1: str, s2: str) -> bool:
    1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    i = 0
    flag = True
    while i < len(list1) and flag:
        if list1[i] == list2[i]:
            i += 1
        else:
            flag == False
    return flag

result=CheckPermutation('abcdefghijkl','bcaedfijhk')
print(result)