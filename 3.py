n=int(input())
val={0,1,2,5,6,8,9}
c=1
num=1
cur=1
while c<=n:
    flag=0
    prev=num
    while num:
        if num%10 in val:
            num=num//10
        else:
            flag=1
            break
    if flag==0:
        cur=prev
        c+=1
    num=prev+1
print(cur)
