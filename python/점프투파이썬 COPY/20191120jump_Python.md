# 딕셔너리



### 1. 딕셔너리 사용하는 방법



#### 1-1. 딕셔너리에서 Key 사용해 Value 얻기

```
grade ={'pey':10,'julliet':99}
print(grade['pey'])

아마 idle 에서는 print 없이 grade['pey']만 입력을 해도 출력이 될 것이다.

결과

10
```



: Key를 사용해서 Value를 구하는 방법이다. 위 예에서 'pey'라는 Key의 Value를 얻기 위해 grade['pey']를 사용한 것처럼 어떤 Key의 Value를 얻기 위해서는 **딕셔너리변수이름[Key]** 를 사용한다. 이 점을 유념을 하며, key에는 숫자도 들어갈 수 있다는 것도 알아두자. (key에느 list 형식은 들어가지 않는다. 단일 형식의 개체 하나만 들어간다.)





### 2. 딕셔너리 함수



#### 2-1. key 리스트 만들기

```
grade ={'pey':10,'julliet':99}
print(grade.keys())

결과

dict_keys(['pey', 'julliet'])

그리고 dict_keys객체를 리스트화 하기 위해서는
list((a.keys()))

결과
['pey', 'julliet']
```



그리고 위와 비슷한 방식으로 value 값을 얻고 싶다면,  변수명.values()













