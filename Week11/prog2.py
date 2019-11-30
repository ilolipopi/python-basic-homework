n=int(input())
c=['']
for i in range(n):
    c.append(True)
for i in range(2,n):
    k=1
    while k*i<n:
        c[k*i]=not c[k*i]
        k+=1
out=[]
for i in range(1,1+n):
    if c[i]:
        out.append(i)
print(*out)
