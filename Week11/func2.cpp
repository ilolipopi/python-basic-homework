def giveChange(money):
    pricelist=[10,5,1]
    pricecount=[]
    print(str(money)+' = ',end='')
    for i in range(3):
        print(str(money//pricelist[i])+'*'+str(pricelist[i]),end='')
        if i!=2:print(' + ',end='')
        money=money%pricelist[i]
    print()
n =  int(input())
for i in range(n):
    giveChange(int(input()))
