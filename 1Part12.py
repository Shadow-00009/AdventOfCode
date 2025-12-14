with open("inp1.txt") as f:
    inp = f.read().splitlines()   
i=50
j=0
count=0
c=int(((inp[j])[1:]))
for j in range(0,4147):
    if((inp[j])[0]=='R'):
        i=i+int(((inp[j])[1:]))%100
        if i>99 and i!=0:
            i=i-100
            count+=1
        elif i==100:
            i=0
    else:
        i=i-int(((inp[j])[1:]))%100
        if i<0:
            i=i+100
            count+=1
    count=count+int(((inp[j])[1:]))//100
    if i==0 and c//100!=1:
        count+=1
    if(j==len(inp)-1):
        break
print(count)