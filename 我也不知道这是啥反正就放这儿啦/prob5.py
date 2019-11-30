raw=list(map(int,input().split(',')))
t=int(input())
i=0
j=0
c=0
for i in range(0,len(raw)):
    for j in range(0,i):
        if raw[i]+raw[j]==t:
            print(j,i)
            c=1
if c==0:print("no answer")
