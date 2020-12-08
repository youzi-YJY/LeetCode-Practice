class AnimalShelf:
    def __init__(self):
        self.elem=[]
    def queue(self,animal):
        self.elem.insert(0,[animal[0],animal[1]])
    def dequeueAny(self):
        ret=[-1,-1]
        if self.elem:
            ret=self.elem.pop()
        return ret
    def dequeueDog(self):
        i=len(self.elem)-1
        ret=[-1,-1]
        while i>0:
            if self.elem[i][1]==1:
                ret=self.elem[i]
                del self.elem[i]
                break
            i-=1
        return ret

    def dequeueCat(self):
        i=len(self.elem)-1
        ret=[-1,-1]
        while i>=0:
            if self.elem[i][1]==0:
                ret=self.elem[i]
                del self.elem[i]
                break
            i-=1
        return ret
