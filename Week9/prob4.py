raw=list(input())
targ=('a','e','i','o','u')
count=0
for i in range(len(raw)):
    if raw[i] in targ:
        count+=1
print(count)
