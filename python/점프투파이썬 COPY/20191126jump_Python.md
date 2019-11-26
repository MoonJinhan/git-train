# 20191126 for문



### for 기본구조



```
for 변수 in 리스트(또는 튜플, 문자열)
수행할 문장 N개
.
.

```



### 기본예제



```
test =['one','two','three']
for i in test:
    print(i)
    
    
결과

one
two  
three

////////////////////////////////////////////////

a = [(1,2),(3,4),(5,6)]
for (first,last) in a :
    print(first+last)
    
결과

3
7 
11

```



### 응용예제



```
score=[90,25,67,45,80]
for i in score:
    if i > 60:
        print('합격')
    else:
        print('불합격')

합격
불합격
합격  
불합격
합격  
```



### for 문과 continue

: for 문에서 continue문을 만나면, for문의 처음으로 돌아가게 된다. 

```

score=[90,25,67,45,80]
num=0
for i in score:
    num = num+1
    if i < 60:
        continue
    print("%d번 학생 축하하빈다. 합격입니다." %num)
        
```



### for문과 range함수

:range함수는 숫자리스트를 자동으로 만들어 줍니다. 그래서 for문과 함께 자주 사용합니다. 예제보시죠.

```
add = 0 
for i in range(1,11):
    add = add+i

print(add)

55
```



위의 예시에서 한 가지 주의해야 할 점은, 1부터 11까지의 숫자가 나오는 것이아니라, 1부터 11미만! 즉 10까지 숫자가 카운트 되게 됩니다.



### 또다른 예제 구구단!



```
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end='')
    print('')
    
24681012141618
369121518212427
4812162024283236
51015202530354045
61218243036424854
71421283542495663
81624324048566472
91827364554637281
```

개인적으로는 구구단을 만드는 과정보다는 저 end함수가 먼가 싶어서 봤다.  end를 넣어 준 이유는 해당 결괏값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서이다. 



그래서 end 함수를 빼버리니.. 아래와 같은 결과를 볼 수 있었다.



```
2
4
6
8
10
12
14
16
18
3
6
.
.
```



### 리스트 내포 사용하기

num의 값들에 2를 곱한 값을 계속해서 저장하는 코드. 이를 간략하게 만들 수 가 있다. 

```
a =[1,2,3,4]
result=[]
for num in a:
    result.append(num*2)
print(result)
```



간략화. 좀 신기하다이.



```
a =[1,2,3,4]
result=[num*2 for num in a]
print(result)

다른 예제

>>> a = [1,2,3,4]
>>> result = [num * 3 for num in a if num % 2 == 0]
>>> print(result)
```



내포 2개이상 사용하기

```
[표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]
```



```
>>> result = [x*y for x in range(2,10) for y in range(1,10)]
>>> print(result)
```

