def function(n,num,diff):#prepinsta accenture question 4 array
    count=0
    for i in range(len(n)):
        if abs(num-n[i])<=diff:
            count+=1
    if count==0:
        return -1

    return count



n=list(map(int,input().split()))
num=int(input())
diff=int(input())
r=function(n,num,diff)
print(r)