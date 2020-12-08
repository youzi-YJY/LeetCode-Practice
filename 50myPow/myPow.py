#递归
class Solution:
    def myPow(self,x,n):
        if n<0:
            n=-n
            return 1/self.help_(x,n)
        return self.help_(x,n)

    def help_(self,x,n):
        if n==0:
            return 1
        if n%2==0:
            return self.help_(x*x,n//2)
        return self.help_(x*x,(n-1)//2)*x

#迭代
class Solution:
    def myPow(self,x,n):
        judge=True
        if n<0:
            n=-n
            judge=False
        final=1
        while n>0:
            if n%2==0:
                x*=x
                n//=2
            final*=x
            n-=1
        return final if judge else 1/final