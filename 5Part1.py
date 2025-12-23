with open("inp5.txt") as f:
    inp1 = f.read().splitlines()
with open("inp52.txt") as g:
    inp2 = g.read().splitlines()
cnt=0
for j in range(len(inp2)):
    for i in range(len(inp1)):
        s=inp1[i]
        index=s.index('-')
        s1=int(s[0:index])
        s2=int(s[index+1:])
        if int(inp2[j]) in range(s1,s2+1):
            cnt+=1
            break

print(cnt)
