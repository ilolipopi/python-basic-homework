r=[0]
c=0
i=0
while r[i]>=0:
    r.append(int(input()))
    i+=1
    if r[i]<60 and r[i]>0:
        c+=1
r.remove(r[i])
if c==0:
    c=",没有学生"
else:
    c=",不及格人数="+str(c)
print("平均分="+str(sum(r)/(i-1))+c)
