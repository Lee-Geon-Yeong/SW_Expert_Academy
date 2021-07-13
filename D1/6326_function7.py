def Factorial(n) :
    if n == 1 : #n이 1이면 1반환
        return 1
    else :
        return n * Factorial(n-1) # n! = n * (n-1)!


n = int(input()) #수 입력
print(Factorial(n)) #함수 실행
