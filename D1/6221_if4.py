rsp = ["가위", "바위", "보"]
Man1 = input()
Man2 = input()
if Man1 == Man2 :
    print("Result : Draw")
else :
    num = 0 
    for i in rsp :
        if Man1 == i :
            if Man2 == rsp[(num + 2) % 3] :
                print("Result : Man1 Win!")
            else :
                print("Result : Man2 Win!")
        else :
            num+=1 
