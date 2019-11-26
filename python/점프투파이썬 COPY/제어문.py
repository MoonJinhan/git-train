#<for>
# test =['one','two','three']
# for i in test:
#     print(i)


# a = [(1,2),(3,4),(5,6)]
# for (first,last) in a :
#     print(first+last)

#Q. "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 
# 합격인지 불합격인지 결과를 보여 주시오."

# score=[90,25,67,45,80]
# num=0
# for i in score:
#     num = num+1
#     if i < 60:
#         continue
#     print("%d번 학생 축하하빈다. 합격입니다." %num)
        


#원래 답

# marks = [90, 25, 67, 45, 80]

# number = 0 
# for mark in marks: 
#     number = number +1 
#     if mark >= 60: 
#         print("%d번 학생은 합격입니다." % number)
#     else: 
#         print("%d번 학생은 불합격입니다." % number)

# #<range 함수>
# add = 0 
# for i in range(1,11):
#     add = add+i

# print(add)
#Q2 . for와 range 함수를 사용하면 소스 코드 단 4줄만으로 구구단을 출력할 수 있다. 
# 들여쓰기에 주의하며 입력해 보자
# num =1
# for i in range(1,10):
#     num = num +1
#     print("%d * %d = %d",  % num,% i,% num*i)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end='')
#     #print('')

#리스트 내포하기
# a =[1,2,3,4]
# result=[]
# for num in a:
#     result.append(num*2)
# print(result)

a =[1,2,3,4]
result=[num*2 for num in a]

print(result)

#<while>
# tree = 0
# while tree <10:
#     tree = tree+1
#     print("나무를 %d번 찍었습니다." % tree)
#     if tree ==10:
#         print("나무가 넘어갑니다.")
#<while ex1>
# prompt ="""
# 1.add
# 2.del
# 3.list
# 4.quit
# Enter num = """

# num=0
# while num != 4:
#     print(prompt)
#     num=int(input())

# coffee =10
# money=300
# while money:
#     print("돈 받았으니 커피를 줍니다.")
#     coffee = coffee-1
#     print("남은 커피의 양은 %d개입니다." %coffee)
#     if coffee==0:
#         print("커피 sold out")
# #         break
# prompt="""
# 커피 = 300원

# 돈을 넣어주세요.
# """
# coffee=10
# money =0
# while print(prompt) == 300:
#     print(prompt)
#     money = int(input())
#     if money == 300:
#         coffee = coffee-1
#     elif money >300:
#         print("거스름 돈을 %d 줍니다." %money)
#     else:
#         print("돈이 모자랍니다.")
    

#<answer>

# coffee = 10
# while True:
    
#     money = int(input("돈을 넣어 주세요.:  "))
#     if money == 300:
#         print("커피를 줍닏나.")
#         coffee = coffee-1
#     elif money>300:
#         print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
#         coffee=coffee-1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee ==0:
#         print("커피가 다떨어졌습니다. 판매를 중지합니다.")
#         break
            
#<<<<if>>>>
# m =True

# if m:
#     print('택스를 타자')
# else:
#     print('돈이 없다.')

#<<<<and, or, not>>>>

# m=2000
# card =True

# if m >= 5000 or card:
#     print(1)
# else:
#     print(2)

#<<<<in>>>>

# print('j' not in 'python')

# p = ['A','B','C']
# if 'A' in p:
#     print('있다.')
# else:
#     print('없다')

# #<<<elif>>>

# p = ['a','b']
# card = True

# if 'm' in p:
#     print("택시를 타고가라")
# elif card:
#     print("역시 택시를 타고 가라")
# else:
#     print("기어가라 영주")