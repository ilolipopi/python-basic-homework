import random
def create( ):
    temp=[]
    global suit
    global d
    for i in range(4):
        for j in range(13):
            temp.append(suit[i]+d[j])
    return(temp)
def shufflecard(pokers):
    return(pokers)
def deal(pokers,n):
    print('第'+str(n)+'个玩家拿到的牌是：',end='')
    print(*pokers[n-1:n-1+20:4],sep=',')
suit=['♥','♠','♦','♣']
d=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
n=int(input())
random.seed(n)
poker=create()
poker=shufflecard(poker)
for i in range(52):
    print('%-4s'%poker[i],end='  ')
    if i%13==12:
        print()
for i in range(1,5):
    deal(poker,i)
