T = int(input())
for x in range(T):
    sum = 0
    odd_input = list(map(int, input().split()))
    for y in odd_input:
        if y % 2 == 1:
            sum += y
    print(f'#{x+1} {sum}')