T=int(input())

for i in range(T):
    n, m = map(int, input().split())
    print(f"#{i+1} {n//m} {n%m}")