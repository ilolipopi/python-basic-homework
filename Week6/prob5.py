d=float(input())
s=[1.0]
i=0
while s[i]>d:
    s.append(s[i]/(i+1))
    i+=1
print(format(sum(s),".6f"))
