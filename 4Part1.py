with open("inp4.txt") as f:
    inp = f.read().splitlines()
final_count=0
for i in range(1,len(inp)-1):
    s=inp[i]
    for j in range(1,len(s)-1):
        count=0
        if s[j]=='@':
            if s[j+1]=='@':
                count+=1
            if s[j-1]=='@':
                count+=1
            if (inp[i-1])[j]=='@':
                count+=1
            if (inp[i-1])[j+1]=='@':
                count+=1
            if (inp[i-1])[j-1]=='@':
                count+=1
            if (inp[i+1])[j]=='@':
                count+=1
            if (inp[i+1])[j+1]=='@':
                count+=1
            if (inp[i+1])[j-1]=='@':
                count+=1
            if count<4:
                final_count+=1
st=inp[0]
for i in range(1,len(st)-1):
    count=0
    if st[i]=='@':
        if st[i+1]=='@':
            count+=1
        if st[i-1]=='@':
            count+=1
        if (inp[1][i]=='@'):
            count+=1
        if (inp[1][i-1]=='@'):
            count+=1
        if (inp[1][i+1]=='@'):
            count+=1
        if count<4:
            final_count+=1

st=inp[len(inp)-1]
for i in range(1,len(st)-1):
    count=0
    if st[i]=='@':
        if st[i+1]=='@':
            count+=1
        if st[i-1]=='@':
            count+=1
        if (inp[len(inp)-2][i]=='@'):
            count+=1
        if (inp[len(inp)-2][i-1]=='@'):
            count+=1
        if (inp[len(inp)-2][i+1]=='@'):
            count+=1
        if count<4:
            final_count+=1


for i in range(1,len(inp)-1):
    count=0
    if inp[i][0]=='@':
        if inp[i][1]=='@':
            count+=1
        if inp[i-1][0]=='@':
            count+=1
        if inp[i-1][1]=='@':
            count+=1    
        if inp[i+1][0]=='@':
            count+=1
        if inp[i+1][1]=='@':
            count+=1
        if count<4:
            final_count+=1

for i in range(1,len(inp)-1):
    count=0
    if (inp[i])[len(inp[i])-1]=='@':
        if inp[i][len(inp[i])-2]=='@':
            count+=1
        if inp[i-1][len(inp[i])-1]=='@':
            count+=1
        if inp[i-1][len(inp[i])-2]=='@':
            count+=1    
        if inp[i+1][len(inp[i])-1]=='@':
            count+=1
        if inp[i+1][len(inp[i])-2]=='@':
            count+=1
        if count<4:
            final_count+=1


if inp[0][0]=='@':
    final_count+=1
if inp[len(inp[0])-1][0]=='@':
    final_count+=1
if inp[len(inp[0])-1][len(inp[0])-1]=='@':
    final_count+=1
if inp[0][len(inp[0])-1]=='@':
    final_count+=1

print(final_count)
