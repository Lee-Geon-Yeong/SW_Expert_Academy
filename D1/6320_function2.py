User1 = input() 
User2 = input() 
User1_pick = input() 
User2_pick = input() 

rsp = ("가위","바위","보")
for i in range(3) : 
    if User1_pick == rsp[i] : 
       if User2_pick == rsp[i] :
           print("{0}(으)로 비겼습니다.".format(User1_pick)) 
           break 
       elif User2_pick == rsp[(i+1)%3] :
           print("{0}가 이겼습니다!".format(User2_pick))
           break 
       else :
           print("{0}가 이겼습니다!".format(User1_pick))
           break 
    else : continue 
