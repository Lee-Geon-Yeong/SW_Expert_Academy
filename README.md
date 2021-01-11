## Python 문법

### 1. 자료형
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
  - 튜플은 한 번 선언된 값을 변경할 수 없다
   - 리스트는 대괄호를 이용하지만, 튜플은 소괄호를 이용한다
    - 튜플 자료형은 그래프 알고리즘을 구현할 때 자주 사용된다
+ 사전 자료형
  - 키와 값을 쌍을 데이터로 가지는 자료형
   - 키 데이터 추출은 keys(), 값 데이터 추출은 values()
+ 집합 자료형


### 2. 조건문

### 3. 반복문

### 4. 함수

### 5. 입출력
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
```

### 6. 주요 라이브러리 문법과 유의점
+ 내장 함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리이다. 파이썬 프로그램을 작성할 때 없어서는 안 될 필수적인 기능을 포함하고 있다.
+ itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. 순열과 조합 라이브러리를 제공한다.
```python
permutations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산.
               permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용.
# 리스트 ['A', 'B', 'C']에서 3개(r=3)를 뽑아 나열하는 모든 경우 출력
from itertools import permutations
data=['A', 'B', 'C']
result=list(permutations(data, 3))
print(result)

combinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산.
               combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용.
# 리스트 ['A', 'B', 'C']에서 2개(r=2)를 뽑아 순서에 상관없이 나열하는 모든 경우 출력
from itertools import combinations
data=['A', 'B', 'C']
result=list(combinations(data, 2))
print(result)

product : permutations와 유사. 중복허용하는 순열 구하기
combinations_with_replacement : combinations와 유사. 중복허용하는 조합 구하기
```

+ heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
```python
heapq.heappush() : 힙에 원소 삽입
heapq.heappop() : 힙에서 원소 꺼냄
```
+ bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.
```python
bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
count_by_range(a, left_value, right_value) : 정렬된 리스트 a에서 값이 [left_value, right_value]에 속하는 데이터의 개수 반환
```
+ collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.
```python
deque : 큐 구현
popleft() : 첫 번째 원소 제거할 때
pop() : 마지막 원소 제거할 때
appendleft(x) : 첫 번째 인덱스에 원소 x 삽입
append(x) : 마지막 인덱스에 원소 x 삽입

counter : 등장 횟수를 세는 기능 제공
```
+ math : 필수적인 수학적 기능을 제공하는 라이브러리이다. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있다.
```
factorial(x) : x!
sqrt(x) : x의 제곱근 반환
gcd(a, b) : a, b의 최대공약수 반환
math.pi 또는 math.e : 파이 또는 자연상수 e 출력
```
### 7. 시간과 메모리 측정
```python
import time
start_time=time.time() # 측정 시작

# 이 부분에 프로그램 소스 코드

end_time = time.time() # 측정 종료
print("time : ", end_time - start_time) # 수행 시간 출력
```
