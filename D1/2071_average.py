T = int(input())

for i in range(T):
    sum=0
    input_list=list(map(int, input().split()))
    for num in input_list:
        sum+=num

    print(f"#{i+1} {round(sum/10)}") 
