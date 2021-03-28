T=int(input())

for i in range(T):
    output_list=list(map(int, input().split()))
    output_max=max(output_list)
    print(f'#{i+1} {output_max}') 

