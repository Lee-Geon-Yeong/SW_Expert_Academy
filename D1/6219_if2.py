num1 = int(input()) 
Deci = 0 
for num2 in range(1,num1+1)  : 

    if num1 % (num2) == 0 : 
        print("%d(은)는 %d의 약수입니다." %(num2,num1))
        Deci += 1 

if Deci == 2 : 
    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (num1, num1))
