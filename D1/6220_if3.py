alp = ord(input()) # chr 변수 하나를 넣으면 그에 맞는 아스키코드 값으로 바꿔주는 함수
if alp >= 97 : #소문자 a의 아스키 코드값은 97, 대문자는 그 이하
    print("%c 는 소문자 입니다." % alp)
else :
    print("%c 는 대문자 입니다." % alp)