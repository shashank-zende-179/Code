def function(n):
    l=list(n)
    for i  in range(len(l)):
        if l[i]=='-':
            l.pop(i)
    l.insert(0,'-')
    a=''.join(l)
    return a



n=map(str,input().split())
r=function(n)
print(r)