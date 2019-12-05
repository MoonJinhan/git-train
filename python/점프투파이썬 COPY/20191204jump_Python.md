# 04 함수 



### 04-1 매개변수 지정하여 호출하기

함수를 호출 할 때 매개변수를 지정할 수도 있다. 

```
def add(a,b):
	return a+b
	
result = add(a=3, b=7)

print(result)

10
```



### 04-2 입력값의 개수를 모를 경우는?

입력값이 정확하게 모를때는 어떻게 하는가?  이럴 경우를 대비해서 아래와 같은 방식으로 코딩을 한다.

```
def 함수이름(*매개변수): 
    <수행할 문장>
    ...
```



#### Q. 여러 개의 입력값을 받는 함수 만들기

다음 예를 통해 여러 개의 입력값을 모두 더하는 함수를 직접 만들어 보자. 예를 들어 `add_many(1, 2)`이면 3을, `add_many(1,2,3)`이면 6을, `add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`이면 55를 돌려주는 함수를 만들어 보자

```python
def add_many(*args):
    result = 0
    for i in args:
        result = result+i
    return result


result = add_many(12,3,4)
print(result)

19

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

55
```



여러 개의 입력을 처리할 때 `def add_many(*args)`처럼 함수의 매개변수로 `*args`만 사용할 수 있는 것은 아니다.



```python
def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul("add",1,4,6)
result1 = add_mul("mul",10,2,3)

print(result)
print(result1)

11
60
```

add_mul 함수는 여러 개의 입력값을 의미하는 `*args` 매개변수 앞에 choice 매개변수가 추가되어 있다.

매개변수 choice에 'add'가 입력된 경우 `*args`에 입력되는 모든 값을 더해서 11를 돌려주고, 'mul'이 입력된 경우 `*args`에 입력되는 모든 값을 곱해서 60을 돌려준다.



#### 키워드 파라미터 예제



```
def kwargs(**kwargs):
  
    return kwargs

print(kwargs(a=1))
print(kwargs(name='foo',age=3))

{'a': 1}
{'name': 'foo', 'age': 3}

신기하게도 딕셔너리 형태로 저장을 한다.
```



입력값 `a=1` 또는 `name='foo', age=3`이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다. 즉 `**kwargs`처럼 매개변수 이름 앞에 `**`을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 `key=value` 형태의 결괏값이 그 딕셔너리에 저장된다.



### 04-3. 함수의 결괏값은 언제나 하나이다

```
def add_and_mul(a,b):
	return a+b,a*b

※ add_and_mul 함수는 2개의 입력 인수를 받아 더한 값과 곱한 값을 돌려주는 함수이다.

result = add_and_mul(3,4)
print(result)

result =(7,12)

```

결괏값은 `a+b`와 `a*b` 2개인데 결괏값을 받아들이는 변수는 result 하나만 쓰였으니 오류가 발생하지 않을까? 당연한 의문이다. 하지만 오류는 발생하지 않는다. 그 이유는 함수의 결괏값은 2개가 아니라 언제나 1개라는 데 있다. add_and_mul 함수의 결괏값 `a+b`와 `a*b`는 튜플값 하나인 `(a+b, a*b)`로 돌려준다. 즉 결괏값으로 (7, 12)라는 튜플 값을 갖게 되는 것이다.

```
result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

7
12
```













