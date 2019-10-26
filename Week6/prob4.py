n=int(input())
i=0
s=[]
h=[]
while i<n:
    s.append('')
    h.append(0.0)
    s[i],h[i]=input().split()
    h[i]=float(h[i])
    i+=1
i=0
while i<n:
    if s[i]=='F':
        print(format(h[i]*1.09,".2f"))
    else:
        print(format(h[i]/1.09,".2f"))
    i+=1

