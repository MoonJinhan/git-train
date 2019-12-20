Q1.주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def is_odd():

    for i in input():
        i=int(i)
        if i%2 == 0:
            print('짝수')
        elif i%2 != 0:
            print('홀수')
    return (i)

print(is_odd())

Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

나의 답
def cal(*args):
    
    res = 0
    result=0
    for i in args:
        
        res += i

        result = res/len(args)
        
    return round(result,2)

print(cal(1,2,3,4,7))

정답
>>> def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
...     result = 0
...     for i in args:
...         result += i
...     return result / len(args)
...
>>> avg_numbers(1, 2)
1.5
>>> avg_numbers(1,2,3,4,5)
3.0

1차 오답 
def cal(*args):
    
    res = 0

    for i in args:
        print(i, end=' ')
i는 잘 들어간다.
        i += i
이렇게 하면, 첫 i 부터 끝 i까지 더하는 것이 아니라
i+i 즉 i *2 를 하는 것과 같은 값이 출력이 된다. 그래서...

        print(i)
        
    return round(res,2)

 숫자를 입력받아 더하여 돌려주는 프로그램이다.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
이 프로그램을 수행해 보자.

첫번째 숫자를 입력하세요:3
두번째 숫자를 입력하세요:6
두 수의 합은 36 입니다
3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

Q3. 정답
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)

Q5
f1 = open("test_3.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test_3.txt",'r')
print(f2.read())
f2.close()


f1 = open('test_7.txt','r')
text = f1.read()
text.replace('java','python')
print(text)