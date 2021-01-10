T=int(input())

for test_case in range(1, T+1):
    nums=list(map(int, input().split()))
    result=0
    for num in nums:
        result=result+num

    num_average=round(result/10)
    print("#%d %d " % (test_case, num_average))