# 재귀함수로 구현
T=int(input())
def plus(n):
    if n==1 :
        return 1
    else:
        return n+plus(n-1)
print(plus(T))

# 수학 계산식 이용
n=int(input())
print(n*(n+1)//2)

# for문 이용
N = int(input())
sum = 0
for i in range(1, N + 1):
    sum += i
print(sum)