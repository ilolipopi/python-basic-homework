def getCircleArea(r):
    import math
    return(math.pi*r*r)
def get_rList(n):
    rList=[]
    for i in range(n):
        rList.append(int(input()))
    return(rList)
n = int(input())
rList = get_rList(n)
for e in rList:
    print('{:10.3f}'.format(getCircleArea(e)))
print(type(rList))
