def Str_Len() : #문자열 길이비교 함수
    Str = input() #문자열 입력
    Str1 = Str.split(', ') #문자열을 (, )콤마+띄어쓰기를 기준으로 나눠 리스트로 배분한다.

    if len(Str1[0]) > len(Str1[1]) : #두개의 문자열 비교이므로 첫번째가 두번째보다 길경우
        print(Str1[0]) #첫번째 출력
    elif len(Str1[0]) < len(Str1[1]) : #반대
        print(Str1[1])

    else : #두 문자열 길이가 같을경우
        print("둘다 같습니다.")

Str_Len()
