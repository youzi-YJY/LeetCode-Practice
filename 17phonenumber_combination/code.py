class Solution(object):
    def letterCombinations(self,digits):
        m={
            '2':list('abc'),
            '3':list('def'),
            '4':list('ghi'),
            '5':list('jkl'),
            '6':list('mno'),
            '7':list('pqrs'),
            '8':list('tuv'),
            '9':list('wxyz'),
        }
        if not digits:return []
        lsl=['']
        for i in digits:
            lsl=[x+y for x in lsl for y in m[i]]
        return lsl