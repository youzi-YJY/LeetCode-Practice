class Solution(object):
    def isValid(self,s):
        '''
        :param s: str
        :return: Boolean True or False
        '''
        dic={'{':'}','[':']','(':')','?':'?'}
        stack=['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()]!=c:
s                return False
        return len(stack)==1