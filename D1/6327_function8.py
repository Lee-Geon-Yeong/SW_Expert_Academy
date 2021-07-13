def square(n) :
    print("square(%d) => %d"%(n,pow(n,2))) #pow(a,b) : a를 b제곱 해주는 pow함수 
Num = list(input())
a = int(Num.pop(0)) 
b = int(Num.pop(-1)) 
square(a)
square(b)
