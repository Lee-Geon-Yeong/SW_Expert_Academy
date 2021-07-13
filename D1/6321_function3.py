a = int(input()) #Prime_Num
Count = 0

if a == 0 or a == 1 : print("소수가 아닙니다.") #a가 0이나 1이면 소수아님
elif a==2 : print("소수입니다.") #2면 소수

for i in range(2,a) : #2부터 a-1까지
    if a % i == 0 : #중간에 한번이라도 나머지가 0이면 소수아님
        print("소수가 아닙니다.")
        break #소수가 아니므로 굳이 반복필요없이 바로 종료
    else :
        if i == a-1 : print("소수입니다.") #i가 a-1 끝까지 갔다면 소수확정
        continue
