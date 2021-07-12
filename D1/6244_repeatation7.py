std_score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
i = 0 # i번째 학생
over_80 = 0 # 80넘는 학생들의 점수  총합
Count = len(std_score) #학생들의 수 Count
while Count > 0 :
    if std_score[i] >= 80 : #80점이 넘는 학생은
       over_80 += std_score.pop(i) #점수 총합에 더해준다 그리고 빼버림
    else :
        i += 1 #i번째 학생 번호증가
    Count-=1
print(over_80)#총합 출력
