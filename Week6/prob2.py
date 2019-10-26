n=int(input())
i=0
l=10**(n-1)
m=l*10
while l<m:
    if (l//10000%10)**n+(l//1000%10)**n+(l//100%10)**n+(l//10%10)**n+(l%10)**n==l:
        print(str(l))
    l+=1


