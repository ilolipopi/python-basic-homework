money=int(input())
def countprice(price):
    global money
    count=0
    while money>=price:
        count+=1
        money-=price
    print(str(count)+'*'+str(price),end='')
print(str(money)+' = ',end='')
countprice(10)
def printconnection():
    print(' + ',end='')
printconnection()
countprice(5)
printconnection()
countprice(1)
