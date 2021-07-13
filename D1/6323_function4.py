Len = int(input())
List = []
for i in range(Len+1) :
    if i == 0 : continue
    elif i == 1 or i == 2 :
        List.append(1)
    else :
        List.append(List[i-3] + List[i-2])
print(List)