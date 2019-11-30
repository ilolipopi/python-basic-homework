def change(x):
    a=list(x)
    if a.pop(0)=='$':
        m=float(str(*a))
        print(str(*a)+'美元 = ',end='')
        print(format(m*6.709,".2f"),end='')
        print('人民币')
    else:
        m=float(str(*a))
        print(str(*a)+'人民币 = ',end='')
        print(format(m/6.709,".2f"),end='')
        print('美元')

x = input()

change(x)
