T = int(input())
# 1. 수를 체크하기 위한 배열 선언

for tc in range(T) :
    N = int(input())
    K = N 
    check = [0]*10
    # 2. 숫자의 길이만큼 for문 돌려서 각 숫자가 check되어있는지 확인
    while True:
        for i in list(map(int, str(N))) :
            if check[i] == 0:
                check[i]+=1
        if 0 not in check :
            print(f'#{tc+1} {N}')
            break
        N = N + K
