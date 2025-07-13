def function(n,m):# q5
    d_b_n=0
    n_d_b_n=0
    for i in range(1,m+1):
        if i%n==0:
            d_b_n=d_b_n + i
        else:
            n_d_b_n=n_d_b_n + i

    result=abs(n_d_b_n - d_b_n)
    return result



n=int(input())
m=int(input())
f=function(n,m)
print(f)