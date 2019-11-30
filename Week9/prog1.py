a=list(input().split(' '))
b=list(input().split(' '))
z=dict(zip(a,b))
listkey=[]
for key in z.keys():
    listkey.append(key)
listkey=sorted(listkey)
out=[]
for key in list(listkey):
    out.append('(\''+key + '\', \'' + str(z[key])+'\')')
print('[',end='')
print(*out,end='',sep=', ')
print(']')
