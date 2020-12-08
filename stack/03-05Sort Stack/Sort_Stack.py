class TwoStcaks:
    def twoStackSort(self,numbers):
        if None==numbers:return None
        if 1==len(numbers):return numbers
        tmp=None
        s1=[]
        s2=[]
        for i in range(len(numbers)):
            tmp=numbers[i]
            while s1 and tmp<s1[-1]:
                s2.append(s1[-1])
                s1.pop()
            s1.append(tmp)
            while s2:
                s1.append(s2[-1])
                s2.pop()
        while s1:
            s2.append(s1[-1])
            s1.pop()
        return s2