# #클래스 

# class Cookie:
#     pass

# a=Cookie()
# b=Cookie()

# print(a)
# print(b)

class FourCal:
    #1차(구조)
    # 클래스 명의 맨 앞자리는 대문자로 해 주는 것이 개발자 끼리의 약속이라고 한다.

    # pass
    #///////////////////////////////////////
    #2차 객체생성
    def setdata(self,first,second):
    
    #setdata 함수를 만들었다. 클래스 안에 구현된 함수는 다른 말로 메서드(Method)라고 부른다.

        self.first = first
        self.second = second



    # def setdata(self, first, second):   # ① 메서드의 매개변수
    # self.first = first              # ② 메서드의 수행문
    # self.second = second            # ② 메서드의 수행문

    def add(self): #더하기 기능
        result = self.first + self.second
        return result
#1차 구조 Fourcal의 인스턴스
a=FourCal()
# print(type(a))

a.setdata(4,2)

#이제 a객체에서 메소 setdata를 통해서 4,2가 들어간다. 
# 확인 : print(a.first)

print(a.add())

# 나머지는 .. pass