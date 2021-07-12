for i in range(1,201) : #1부터 200까지
    if i % 7 == 0 and (i % 5) != 0 : #7로 나눈 나머지가 0이면서 5로 나눈 나머지가 0이 아님
        if i==7 :
            print('' , end='') #단 첫번째는 ,(콤마)로 시작하지 않음
        else :
            print(',',end='') #중간중간 ,(콤마)삽입 후 글 띄우는 엔터(enter) 삭제
        print(i,end='')
