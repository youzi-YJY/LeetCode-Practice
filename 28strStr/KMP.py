#coding=utf-8
def kmp_match(s,p):
    m=len(s)
    n=len(p)
    cur=0#起始指针
    table=partial_table(p)
    while cur<= m-n:
        for i in range(n):
            if s[i+cur]!=p[i]:
                cur+=max(i-table[i-1],1)
                break
            else:
                return True
    return False

def partial_table(p):
    prefix=set()
    postfix=set()
    ret=[0]
    for i in range(1,len(p)):
        prefix.add(p[:i])
        postfix={p[j:i+1] for j in range(1,i+1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret

print(partial_table("ABCDABD"))
print(kmp_match("BBC ABCDAB ABCDABCDABDE","ABCDABD"))