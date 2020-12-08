class Solution:
    def divide(self,divid:int,dior:int)->int:
        res=0
        sign=1 if divid ^ dior>=0 else -1
        divid=abs(divid)
        dior=abs(dior)
        while divid>dior:
            tmp,i=dior,1
            while divid>=tmp:
                divid-=tmp
                res+=i
                i<<=1
                tmp<<=1
        res=res*sign
        return min(max(-2**31,res),2**31-1)