def Find_Num(a,n) : #a는 리스트, n은 찾고자하는 특정 value
    if a.count(n) == 0 : #a리스트에서 n의 개수가 0일 경우 False
        print("{0} => {1}".format(n, False))
    else :#a리스트에서 n의 개수가 0이 아닐 경우 True
        print("{0} => {1}".format(n, True))

A = [2,4,6,8,10]
print(A)
Find_Num(A,5)
Find_Num(A,10)