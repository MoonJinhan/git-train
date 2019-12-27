# 모듈



모듈은 함수나 변수 또는 클래스를 모아 놓은 파일이다. 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 한다.  그러면, 아래에서 바로 모듈을 만들어보고, 사용해 보자.



### 모듈만들기

```
def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
```



### 모듈 실행 1

```
import moduel_test as mod1

print(mod1.add(3,4))
print(mod1.sub(4,3))

7
1
```



과정

1. 모듈 만들기(함수를 만들듯이)
2. import 모듈 이름 as 간소화할 이름
3. 모듈 속에 있는 함수를 사용
4. 완료



### 모듈 실행 2

```
from moduel_test import add

print(add(2,3))
print(sub(3,2))
```



위의 방식은 moduel_test에 있는 add 함수만 빼온것인데, 궁금해서 sub함수를 사용해 보았다.

```
결과
5
Traceback (most recent call last):
  File "c:/Users/user/Documents/DocFile_Programming_note/python/점프투파이썬 COPY/test.py", line 130, in <module>
    print(sub(3,2))
NameError: name 'sub' is not defined
```



add 의 결과는 잘 나오나, sub는 import 하지 않았으므로, 에러가 발생하는 것을 볼 수 있다.



```
만약 두가지를 다 사용하고 싶다면,

from moduel_test import add,sub

or

from moduel_test import *

를 사용한다.
```



### if __name__ == "__main__": 의 의미



`if __name__ == "__main__"`을 사용하면 `C:\doit>python mod1.py`처럼 직접 이 파일을 실행했을 때는 `__name__ == "__main__"`이 참이 되어 if문 다음 문장이 수행된다. 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 `__name__ == "__main__"`이 거짓이 되어 if문 다음 문장이 수행되지 않는다.





### 클래스나 변수 등을 포함한 모듈



#### 클래스, 함수 

```
PI = 3.141592

class Math:
    def solv(self,r):
        return PI * (r ** 2)

# ** 제곱 맨날 까먹네 ;;
def add(a,b):
    return a+b
```



#### 입력

```
import moduel_test as mod1

#1
print(mod1.add(2,3))
print(mod1.PI)

#2
a = mod1.Math()

print(a.solv(2))

print(mod1.solv(2))
```



#### 출력 #1

```
5
3.141592
```



평소와 같이 출력이 된다. 하지만, 클래스 내부에 있는 함수를 사용하기 위해서는 다른 방식이 필요하다.



#### 출력 #2

```
12.566368

Traceback (most recent call last):
  File "c:/Users/user/Documents/DocFile_Programming_note/python/점프투파이썬 COPY/test.py", line 134, in <module>       
    print(mod1.solv(2))
AttributeError: module 'moduel_test' has no attribute 'solv'
PS C:\Users\user\Documents\DocFile_Programming_note\python\점프투파이썬 COPY> 
```



위 예처럼 모듈 안에 있는 클래스를 사용하려면 "."(도트 연산자)로 클래스 이름 앞에 모듈 이름을 먼저 입력해야 한다. 그렇지 않으면, 2번째 print(mod1.solv(2)) 처럼 에러가 발생한다. 













