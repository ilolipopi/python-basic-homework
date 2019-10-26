m,n=map(int,input().split(","))
r=min(m,n)
x=max(m,n)
while m%r or n%r:
    r-=1
while x%m or x%n:
    x+=1
print("GCD:"+str(r)+", LCM:"+str(x))

