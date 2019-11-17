# 20191117 튜플~

튜플은 리스트하고 비슷하, 다른 점이 있다.



- 리스트는 []로 둘러싸지만, 튜플은 ()으로 둘러싼다.
  - ()을 쓰지만 생략해도 무방하다.
- 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그값을 바꿀 수 없다.



**튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는가 여부이다.** 즉 리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다. 따라서 프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고 싶지 않다면 주저하지 말고 튜플을 사용해야 한다. 이와는 반대로 수시로 그 값을 변화시켜야할 경우라면 리스트를 사용해야 한다. 실제 프로그램에서는 값이 변경되는 형태의 변수가 훨씬 많기 때문에 평균적으로 튜플보다는 리스트를 더 많이 사용한다. 



튜플의 삭제와 변경함에 있어서,애러가 실제로 발생을 하는지 알아본다.

```
t1=(1,2,'a','b')
del t1[0]

print(t1)
```

에라... 삭제

```
Traceback (most recent call last):
  File "C:/Users/user/Documents/DocFile_Programming_note/python/점프투파이썬 COPY/test.py", line 2, in <module>
    del t1[0]
TypeError: 'tuple' object doesn't support item deletion
```



```
t1=(1,2,'a','b')
t1[0]=2

print(t1)
```

에라....변경

```
Traceback (most recent call last):
  File "C:/Users/user/Documents/DocFile_Programming_note/python/점프투파이썬 COPY/test.py", line 2, in <module>
    t1[0]=2
TypeError: 'tuple' object does not support item assignment
```



그외 인덱싱, 슬라이싱, 연산, 길이구하는 함수 len까지 모두 같으니 궁금하다면, 구글링 ㄱㄱ



## 딕셔너리

(나를 고생시킨 녀석)



딕셔너리 간단하게 말하자면, 대응관계를 나타내는 자료형이다. 대응관계란 "이름" = "홍길동" 과 같은 구조(key = value)를 가진 데이터를 말한다. 이를 연관배열 혹은 해시라고 한다. 딕셔너리는 key을 통해서 보고싶은 부분만 보는 것이다. 



#### 딕셔너리 구조

```
{key1 : value1,..... key n : value n ....}

ex) {'name' : 'kevin','age':'18','country':'USA'}

이 외에도 리스트를 value 값으로 사용 할 수 있다.
```



#### 딕셔너리 쌍 추가, 삭제하기

```python
a = {1:'a'}
print(a)
a[2]='b'
print(a)
```

```
{1: 'a'}
{1: 'a', 2: 'b'}
```



위의 결과를 토대로 보면  **변수명[key] = value** 이 되는 것을 확인 할 수 있다. 

```
del a[1]
a

{2: 'b'}
```

 del 변수명[key] 입력을 해주면 지워주는 것을 확인 했다.









