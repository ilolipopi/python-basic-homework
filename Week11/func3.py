def printYanghui(n):
    line=0
    tri=[]
    while line<n:
        for i in range(n-line-1):
            print(' ',end='')
        temp=[]
        for i in range(line+1):
            if line!=0 and i!=0 and i != line: temp.append(tri[line-1][i]+tri[line-1][i-1])
            else: temp.append(1)
        tri.append(temp)
        print(*temp,end=' \n')
        line+=1
n = int(input())        
printYanghui(n)
