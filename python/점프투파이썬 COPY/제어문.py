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

coffee = 10
while True:
    
    money = int(input("돈을 넣어 주세요.:  "))
    if money == 300:
        print("커피를 줍닏나.")
        coffee = coffee-1
    elif money>300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
        coffee=coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee ==0:
        print("커피가 다떨어졌습니다. 판매를 중지합니다.")
        break
            
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