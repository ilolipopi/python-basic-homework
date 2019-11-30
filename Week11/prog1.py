n=int(input())
def ptl(n):
    for i in range(n):
        print('+ - - - - ',end='')
    print('+')
def pti(n):
    for i in range(n):
        print('|         ',end='')
    print('|')
for i in range(n):
    ptl(n)
    for j in range(4):
        pti(n)
if n!=0:ptl(n)
