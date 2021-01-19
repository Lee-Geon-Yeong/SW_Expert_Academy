N=int(input())

input_list=list(map(int, input().split()))

input_list.sort()

print(input_list[N//2])