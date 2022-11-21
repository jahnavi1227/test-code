n=int(input())
a=''
while n:
    a=a+str(n%3)
    n=n//3
print(a[::-1])
