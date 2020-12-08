# -*-coding:utf-8 -*-
class Solution:
    def addbinary(self,a,b):
        '''
        :param a: binary string
        :param b: binary string
        :return:  sum of a and b
        Python bin function:
        bin() 返回一个整数 int 或者长整数 long int 的二进制表示
        前面会带有0b需要祛除
        Python int function:
        class int(x, base=10) x：字符串或者数字 base-进制数 默认为十进制
        '''
        return bin(int(a,2)+int(b,2))[2:]
