# 사용자 입력과 출력



### 1. 사용자 입력

사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때는 어떻게 해야 할까? 



####  1-1. input의 사용



```
a = input()

print(a)

입력: life is too short, you need python 
결과: life is too short, you need python 

참고: input은 입력되는 모든 것을 문자열로 취급한다.

프롬프트를 띄워서 사용자 입력받기

a = input('앵무새 입니다.')

print(a)

입력: 앵무새 입니다.프롬프트를 띄워서 사용자 입력받기

출력: 프롬프트를 띄워서 사용자 입력받기

```



### 2. print 자세히 알기



#### 2-1 : 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다

```
print("life" "is" "too short") # ①

print("life"+"is"+"too short") # ②

결과
lifeistoo short
lifeistoo short
```



#### 2-2 :문자열 띄어쓰기는 콤마로 한다

```
print("life","is","too short")
life is too short
```



#### 2-3한 줄에 결괏값 출력하기

```
for i in range(10):
    print(i,end=' ')

0 1 2 3 4 5 6 7 8 9

for i in range(10):
    print(i)
0
1
2
3
4
5
6
7
8
9  
    
```



# 파일 생성하기

```
f = open('경로/test.txt','w')
f.close()
```



open() 은 파일을 생성할 수 있는 파이썬 내장 함수이다. 

>  파일객체 = open(파일 이름, 파일 열기 모드)



| 파일열기모드 | 설명                                                       |
| :----------- | :--------------------------------------------------------- |
| r            | 읽기모드 - 파일을 읽기만 할 때 사용                        |
| w            | 쓰기모드 - 파일에 내용을 쓸 때 사용                        |
| a            | 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 |



```
f = open('test_2.txt','w')
f.close()
```



![1576564918384](assets/1576564918384.png)

test_2.txt파일이 생성이 된 것이 확인 되었다. 그리고 디렉토리를 추가하고 싶다면 / 를 쓰고 앞에 해당 디렉토리를 써주면 된다. 그리고 f.close 는 써줘도 되고, 안 써줘도 된다. 하지만, 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려면, 오류가 발생하기 때문에, 이때는 대도록이면 close 함수를 사용해 주는 것이 좋다.\



#### 파일을 쓰기 모드로 열어 출력값 적기

```
f = open('test_2.txt','w')
for i in range(1,11):
    data = "%d번째 줄 입니다.\n" % i
    f.write(data)
f.close()

결과
test_2.txt의 내부

1번째 줄 입니다.
2번째 줄 입니다.
3번째 줄 입니다.
4번째 줄 입니다.
5번째 줄 입니다.
6번째 줄 입니다.
7번째 줄 입니다.
8번째 줄 입니다.
9번째 줄 입니다.
10번째 줄 입니다.

///////////////////////////// 아래는 터미널에서 출력 위에는 test_2.txt내부에 쓰여짐

for i in range(1,11):
    data="%d번째 줄입니다.\n" % i
    print(data)
1번째 줄입니다.

2번째 줄입니다.

3번째 줄입니다.

4번째 줄입니다.

5번째 줄입니다.

6번째 줄입니다.

7번째 줄입니다.

8번째 줄입니다.

9번째 줄입니다.

10번째 줄입니다.
```



### 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법



### 1. readline()함수 사용하기



```
f = open('C:/Users/user/Documents/DocFile_Programming_note/python/점프투파이썬 COPY/test_2.txt','r')
line = f.readline()
print(line)
f.close()

1번째 줄 입니다.
위의 코드로는 제일 첫번째에 있는 한 줄만 출력이 가능하다. 만약 내부에 있는 모든 문장을 불러오고 싶다면,아래와 같은 코드를 해주면된다.


while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

인덴트 에러나서 좀 걸렸네요. 가르쳐준 선생님이 하시는 말씀이, 인덴트 에러가 났을 경우에는 spacebar 4번 혹은 전체 드레그해서 인덴트 체크를 하라고 하시네용
```



#### 2. realines()함수 사용하기

```
f = open("C:/Users/user/Documents/DocFile_Programming_note/python/점프투파이썬 COPY/test_2.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

1번째 줄 입니다.

2번째 줄 입니다.

3번째 줄 입니다.

4번째 줄 입니다.

5번째 줄 입니다.

6번째 줄 입니다.

7번째 줄 입니다.

8번째 줄 입니다.

9번째 줄 입니다.

10번째 줄 입니다.
```



### read() 

```
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

data 전체를 읽어온다.
```





### with문과 함께 사용하기

지금까지 살펴본 예제를 보면 항상 다음과 같은 방식으로 파일을 열고 닫아 왔다.

```
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
```

파일을 열면 위와 같이 항상 close해 주는 것이 좋다. 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까? 파이썬의 with문이 바로 이런 역할을 해준다. 다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다.

```
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
```

위와 같이 with문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다.









