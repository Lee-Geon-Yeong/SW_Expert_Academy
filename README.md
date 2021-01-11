## Python 문법

1. 자료형
+ 정수형
+ 실수형
```python
# 코딩테스트에서 최단경로 문제에서는 도달할 수 없는 노드에 대하여 최단 거리 무한(1NF)으로 설정. 
최단 경로로 가능한 최댓값이 10억 미만이라면 무한(1NF)을 표현할 때 10억을 이용할 수 있다.
이 때 일일이 10억을 특정 변수에 입력하지 않고 지수표현방식인 1e9로 표현
1e9 -> 유효숫자e지수 = 유효숫자*10지수 -> 1,000,000,000(10억)
```
```
round(a, 4)는 a를 소수점 5째 자리에서 반올림, 2번째 인자 생략하면 소수점 1째 자리에서 반올림
```
+ 수 자료형의 연산
```
/ 나누기(실수형 반환)
// 몫
```
+ 리스트 자료형
```python
# 코딩테스트에서 크기가 n인 1차원 리스트 초기화 할 때 
n=10
a=[0]*n
print(a)
```
```python
# 코딩테스트에서 N*M 크기의 2차원 리스트 초기화
n=3
m=4
array= [[0]*m for _ in range(n)]
print(array)
```
+ 리스트 관련 기타 메서드
```
변수명.append() 리스트에 원소 하나 삽입
변수명.sort() 오름차순 정렬
변수명.sort(reverse=True) 내림차순 정렬
변수명.reverse() 리스트의 원소의 순서를 모두 뒤집어놓음
변수명.insert(삽입할 위치 인덱스, 삽입할 값) 특정한 인덱스 위치에 원소를 삽입할 때 사용
변수명.count(특정 값) 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용
변수명.remove(특정 값) 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거
# 특정한 값을 모두 제거하려는 경우
a=[1,2,3,4,5,5,5]
remove_set={3,5}
result= [i for i in a if i not in remove_set]
print(result)
```
+ 문자열 자료형
+ 튜플 자료형
-튜플은 한 번 선언된 값을 변경할 수 없다
-리스트는 대괄호를 이용하지만, 튜플은 소괄호를 이용한다
-튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용된다
+ 사전 자료형
-키와 값을 쌍을 데이터로 가지는 자료형
-키 데이터 추출은 keys(), 값 데이터 추출은 values()
+ 집합 자료형

2. 조건문

3. 반복문

4. 함수

5. 입출력
```python
# 데이터의 개수 입력
n=int(input())
# 각 데이터를 공백으로 구분하여 입력
data=list(map(int, input().split()))
# 공백을 기준으로 구분하여 적은 수의 데이터 입력(n,m,k)
n, m, k=map(int, input().split())
```
```python
#입력의 개수가 많은 경우 sys라이브러리에 정의되어 있는 sys.stdin.readline() 함수 이용
 sys라이브러리를 사용할 때는 한 줄 입력을 받고 나서 rstrip() 함수를 꼭 호출해야 한다. 
 readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거
 하려면 rstrip() 함수를 사용해야 한다
import sys
data=sys.stdin.readline().rstrip()
print(data)
```
```python
#문자열+정수형 출력은 f-string 문법 사용
answer=7
print(f"정답은 {answer}입니다.")
