# 클래스



### 1. 클래스의 상속

어떤 클래스를 만들 때, 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다. 백문이 불여일견. 이번에는 예제를 통해서 제곱을 하는 계산기를 만들어보려한다. 



기본 공식 :  class 클래스 이름(상속할 클래스 이름)

```
class MoreFourCal(FourCal):
	pass
	
b = MoreFourCal()
b.setdata(4,3)
print(b.add())

예제에서는 setdata를 쓰지 않았는데, 왜 그럴까? 집에서 실습을 하면 에러가 나온다.
```



제곱을 구하는 계산기

```
class MoreFourCal(FourCal):

    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal()
b.setdata(4,3)

print(b.pow())

64
```



### 2. 메서드 오버라이딩



```

class FourCal:

    def setdata(self,first,second):
    
    
        self.first = first
        self.second = second


    def add(self): #더하기 기능
        result = self.first + self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
         


class MoreFourCal(FourCal):

    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

b = MoreFourCal()

b.setdata(4,0)

print(b.div())

답: 0
```



위의 코드를 보면 FourCal 안에 div 함수가 존재합니다. 그런데 아래에서 보면 div함수를 이용해서 함수를 다시 썼다. 이렇게 FourCal가 부모 클래스(상속한 클래스)에서 MoreFourCal로 자식 클래스(상속 받은 클래스)로 함수를 가지고 오는 것을 메서드 오버라이딩(덮어쓰기)이라고 한다.

































