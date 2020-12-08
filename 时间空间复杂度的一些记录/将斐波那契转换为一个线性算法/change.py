'''
斐波那契数列的前两个数都是1，并且此后的每一个数都是前面两个数的加和
如果n至少是第3个斐波那契数字的话，新的算法就开始了一个循环
执行两个替换，第一个数变为了第二个数，第二个数变为了刚才计算的加和
这样一来，改函数新版本的性能已经提升到了线性阶
'''
class Solution:
    def fib(self,n,counter):
        sum=1
        first=1
        second=1
        count=3
        while count <=n:
            counter.increment()
            sum=first+second
            first=second
            second=sum
            count+=1
        return sum
    '''
    def fib(n):
        if n < 3:
            return 1
        else:
            return fin(n-1)+fib(n-2)
    是一个指数级的O(k^n)的算法，递归的fib函数调用树的底部并不是完全填满的，
    但是其调用树在形状上接近于一个完全平衡树，会导致fib函数成为指数级的算法，k接近于1.63.
    '''