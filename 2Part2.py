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
            elif mid==6:
                if ((str(j)[0:2]==str(j)[2:4]) and (str(j)[0:2]==str(j)[4:])):
                    sum+=j
            elif mid==10:
                if ((str(j)[0:2]==str(j)[2:4]) and (str(j)[0:2]==str(j)[4:6])and (str(j)[0:2]==str(j)[6:8])and (str(j)[0:2]==str(j)[8:])):
                    sum+=j
        elif mid==3:
            if j%111==0:
                sum+=j
        elif mid==5:
            if j%11111==0:
                sum+=j
        elif mid==7:
            if j%1111111==0:
                sum+=j
        elif mid ==9:
            if j%111111111==0 or ((str(j)[0:3]==str(j)[3:6]) and (str(j)[0:3]==str(j)[6:])):
                sum+=j
print(sum)