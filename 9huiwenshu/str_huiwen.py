'''
#Use of String
class Solution(object):
    def huiwen(self,num:int):
        return str(num)==str(num)[::-1]'''


#Use of numberfunction
class Solution(object):
    def IsPalindrome(self,number:int):
        if number<0 or not number%10 and number:return False
        revertedNumber=0
        while number>revertedNumber:
            #后半部分的最后一位*10加上后半部分倒数第二位组成后半部分
            revertedNumber=revertedNumber*10+number%10
            number//=10
        return number==revertedNumber or number==revertedNumber//10