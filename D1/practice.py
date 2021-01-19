T=int(input())

for i in range(T):
    input_list=input()
    check=True
    if 1<=int(input_list[4:6])<=12:
        if input_list[4:6]=='04' or input_list[4:6]=='06' or input_list[4:6]=='09' or input_list[4:6]=='11':
            if 1>int(input_list[6:8]) or int(input_list[6:8])>30:
                check=False
        elif input_list[4:6]=='02':
            if 1>int(input_list[6:8]) or int(input_list[6:8])>28:
                check=False
        else:
            if 1>int(input_list[6:8]) or int(input_list[6:8])>31:
                check=False
    else:
        check=False

    if check==True :
        print(f"#{i+1} {input_list[0:4]}/{input_list[4:6]}/{input_list[6:8]}")
    else:
        print(f"#{i+1} -1") 
