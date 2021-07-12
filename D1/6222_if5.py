letter = ord(input())
if not (65 <= letter <= 90 or 97<=letter<=122) : #65~90 대문자 A~Z , 97~122 소문자 a~z 아니면 그냥 출력
    print("%c" % letter)
elif letter <= 90 : #대문자인경우
    print("%c(ASCII: %d) => %c(ASCII: %d)" % (letter,letter,letter+32,letter+32)) #대문자 소문자 아스키코드 차이값 32
else : #소문자인경우
    print("%c(ASCII: %d) => %c(ASCII: %d)" % (letter, letter, letter - 32, letter - 32))
