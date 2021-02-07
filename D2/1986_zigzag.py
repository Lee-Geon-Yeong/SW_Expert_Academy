for i in range(int(input())):
    N=int(input())
    sum=0
    for j in range(1, N+1):
        if (j)%2==1:
            sum=sum+j
        else:
            sum=sum-j
    print(f"#{i+1} {sum}")
