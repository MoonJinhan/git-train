# print(abs(-3.1))
# abc 절댓값을 돌려주는 함수

# print(all(1))
# TypeError: 'int' object is not iterable
#궁금해서 리스트형을 지우고 int 형 1 하나만 넣어줬다. 그랬더니 에러 ..

# print(all([1,2,3,4]))
# True

# all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
# ※ 반복 가능한 자료형이란 for문으로 그 값을 출력할 수 있는 것을 의미한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다

#any(x)는 x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.
# print(any([1,2,3,0]))

# print(chr(97))
# a

# print(dir([1,2,3]))

# print(divmod(7,3))
# 7/3 = 2 나머지 1 출력
# (2, 1)

# for i, name in enumerate(['body','foo','bar']):
#     print(i,name)

# 0 body
# 1 foo
# 2 bar

# enumerate 는 열거하다라는 뜻을 가지고 있다. 이 함수는 순서가 있는 자료형(리스트 튜플 문자열)
# 을 입력으로 받아 인덱스값을 포함하는 enumerate 객체를 돌려준다. enumerate 함수는 
# 일반적으로 for 문과 같이 사용한다.

# 장점 : 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다. -> 위치 확인에 용의

# print(eval('1+2'))
# 3
# eval(expression )은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.

# print(type(eval("'hi'+'i'")))
# print('hi'+'A')

# hii
# <class 'str'>
# hiA

# 문자끼리 더할 때는 같은 역할을 한다. 
#  eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.

# def positive(l):
#     result = []
#     for i in l:
#         if i > 0:
#             result.append(i)
  
            
#     return result

# print(positive([1,-3,2,0,-5,6]))

# 위의 함수를 통해서 우리는 양수의 수만 출력할 수 있다.

# filter 함수는 첫 번째 인수로 함수 이름을, 
# 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 
# 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.

# def positive(x):
#     return x>0
# print(list(filter(positive, [1,-3,2,0,-5,6])))

# 식: filter(함수 이름 ,[리스트 형의 입력])
#위의 함수에서 사용한 것 처럼 길게 함수를 쓸 필요가 없다. 

# print(hex(265))
# 0x109

# a = input()

# print(int('3'))

# int는 어떤 형태든 정수로 반환한다.

# class Person: pass

# a = Person()
# print(isinstance(a,Person))

# True
# b = Person()
# print(isinstance(b,Person))
# ???

# map(f,iterable)  f = 함수 , iterable = 반복가능한 자료형
#map 은 입력받은 자료형의 각요소를 함수 f가 수행한 결과를 묶어서

# def two_times(numberList):
#     result = []
#     for number in numberList:
#         result.append(number*2)
#     return result

# result = two_times([1,2,3,4])
# print(result)

# def two_times(x):
#     return x*2

# print(list(filter(two_times,[1,2,3,4])))    
# print(list(map(two_times,[1,2,3,4])))

# 순간적으로 맵과 필터의 차이가 무엇인가? 아리송해서 찾아보았다. 나만 그런 것이 아닌가보다.
#예: https://wikidocs.net/22803