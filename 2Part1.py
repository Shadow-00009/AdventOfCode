with open("inp2.txt") as f:
    inp = f.read().split(",")
sum=0
for i in range(len(inp)):
    s=inp[i]
    index=s.index('-')
    s1=s[0:index]
    s2=s[index+1:]
    for j in range(int(s1),int(s2)+1):
        mid=len(str(j))
        if mid%2==0:
            if str(j)[0:((mid//2))]==str(j)[((mid//2)):]:
                sum+=j
print(sum)