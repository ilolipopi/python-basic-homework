def CountDigit(digit,number):
    s=list(str(digit))
    count=0
    for i in range(len(s)):
        if s[i] not in list(map(str,list(range(10)))):continue
        elif int(eval(s[i]))==number:
            count+=1
    return(count)
number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)
