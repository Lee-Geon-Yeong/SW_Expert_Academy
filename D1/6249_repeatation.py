num = input() #양의 정수 생성
CountNum = []
A = []
for i in range(10) :
    A.append(str(i))
print(" ".join(A))
    # print(i, end = " ") # 0~9까지 예시

for j in range(10) :
    CountNum.append(str(num.count(str(j)))) #num은 str인데 j는 정수니까 같은 str로 형변환, 후 그에 맞는 숫자 개수세기
print(" ".join(CountNum))
