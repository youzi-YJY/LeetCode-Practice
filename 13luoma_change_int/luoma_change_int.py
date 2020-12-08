class Sloution(object):
    def romanToInt(self,s:str):
        roman_nums={'M':1000,'C':500,'L':100,'X':10,'V':5,'I':1}
        num=0
        for i in range(len(s)-1):
            if roman_nums[s[i]]>=roman_nums[s[i+1]]:
                num+=roman_nums[s[i]]
            else:
                num-=roman_nums[s[i]]

        last_num=s[len(s)-1]
        num+=roman_nums[last_num]
        return num