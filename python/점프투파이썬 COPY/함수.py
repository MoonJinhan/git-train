# def add(a,b):
#     print("%d,%d의 합은 %d입니다." % (a,b,a+b))

# c = add(3,4)
# print(c)

# def add(a,b):
# 	return a+b

# result = add(a=3, b=7)
# print(result)

#매개변수 지정하여 호출하기가 왜 필요한가요?

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result+i
#     return result


# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

# def add_mul(choice,*args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul("add",1,4,6)
# result1 = add_mul("mul",10,2,3)

# print(result)
# print(result1)

# def kwargs(**kwargs):
  
#     return kwargs

# print(kwargs(a=1))
# print(kwargs(name='foo',age=3))

def add_and_mul(a,b):
    return a+b,a*b

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)