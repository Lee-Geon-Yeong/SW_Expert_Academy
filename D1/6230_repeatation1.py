std = [88,30,61,55,95]
for score in std :
    print("{0}번 학생은 {1}점으로 ".format(std.index(score)+1,score),end = "")
    if score >= 60 :
        print("합격입니다.")
    else :
        print("불합격입니다.")