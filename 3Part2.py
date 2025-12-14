with open("inp3.txt") as f:
    inp = f.read().splitlines()
sum=0
for i in range(len(inp)):
    a=inp[i]
    lst=[]
    for j in range(len(a)):
        lst.append(int(a[j]))
    tm=lst

    lst1=[]
    for j in range(len(a)-11):
        lst1.append(int(a[j]))
    max1=max(lst1)

    ind1=tm.index(max1)
    lst2=[]
    for j in range(ind1+1,len(a)-10):
        lst2.append(int(a[j]))
    max2=max(lst2)

    ind2=tm.index(max2,ind1+1,)
    lst3=[]
    for j in range(ind2+1,len(a)-9):
        lst3.append(int(a[j]))
    max3=max(lst3)

    ind3=tm.index(max3,ind2+1,)
    lst4=[]
    for j in range(ind3+1,len(a)-8):
        lst4.append(int(a[j]))
    max4=max(lst4)

    ind4=tm.index(max4,ind3+1,)
    lst5=[]
    for j in range(ind4+1,len(a)-7):
        lst5.append(int(a[j]))
    max5=max(lst5)

    ind5=tm.index(max5,ind4+1,)
    lst6=[]
    for j in range(ind5+1,len(a)-6):
        lst6.append(int(a[j]))
    max6=max(lst6)

    ind6=tm.index(max6,ind5+1,)
    lst7=[]
    for j in range(ind6+1,len(a)-5):
        lst7.append(int(a[j]))
    max7=max(lst7)

    ind7=tm.index(max7,ind6+1,)
    lst8=[]
    for j in range(ind7+1,len(a)-4):
        lst8.append(int(a[j]))
    max8=max(lst8)

    ind8=tm.index(max8,ind7+1,)
    lst9=[]
    for j in range(ind8+1,len(a)-3):
        lst9.append(int(a[j]))
    max9=max(lst9)

    ind9=tm.index(max9,ind8+1,)
    lst10=[]
    for j in range(ind9+1,len(a)-2):
        lst10.append(int(a[j]))
    max10=max(lst10)

    ind10=tm.index(max10,ind9+1,)
    lst11=[]
    for j in range(ind10+1,len(a)-1):
        lst11.append(int(a[j]))
    max11=max(lst11)

    ind11=tm.index(max11,ind10+1,)
    lst12=[]
    for j in range(ind11+1,len(a)):
        lst12.append(int(a[j]))
    max12=max(lst12)


    num=str(max1)+str(max2)+str(max3)+str(max4)+str(max5)+str(max6)+str(max7)+str(max8)+str(max9)+str(max10)+str(max11)+str(max12)
    print(num)
    sum=sum+int(num)
print(sum)
