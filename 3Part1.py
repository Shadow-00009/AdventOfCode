with open("inp3.txt") as f:
    inp = f.read().splitlines()
sum=0
for i in range(len(inp)):
    a=inp[i]
    lst=[]
    for j in range(len(a)-1):
        lst.append(int(a[j]))
    tm=lst
    max1=max(lst)
    ind=tm.index(max1)
    lst1=[]
    for j in range(ind+1,len(a)):
        lst1.append(int(a[j]))
    max2=max(lst1)
    num=(max1*10)+max2
    print(num)
    sum+=num
print(sum)
