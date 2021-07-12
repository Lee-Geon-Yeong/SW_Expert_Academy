arr = [] #join함수를 위해 arr리스트 생성
for i in range(100,301) :
    a = i // 100 #100의자리. //슬래시 두개는 정수형 나눗셈을 의미한다
    b = (i-100*a) // 10 #10의자리
    c = (i-100*a-10*b) #1의자리

    if a % 2 == 0 and b % 2 ==0 and c % 2 == 0 :
        arr.append(str(i))
print(",".join(arr))