T = int(input())

for i in range(T):
    a, b = list(map(int, input().split()))
    if a > b:
        print("#{} >".format(i + 1))
    elif a == b:
        print("#{} =".format(i + 1))
    else:
        print("#{} <".format(i + 1))

 
# def solution(a, b):
#     if a > b:
#         return '>'
#     elif a == b:
#         return '='
#     else:
#         return '<'
#
#
# if __name__ == '__main__':
#     cnt = int(input())
#     for i in range(cnt):
#         a, b = list(map(int, input().split()))
#         print("#%d %s" % (i + 1, solution(a, b)))
