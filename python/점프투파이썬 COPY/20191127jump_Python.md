20191128 연습문제



```
#<연습문제>
Q1
a = "Life is too short, you need python"

if "wife" in a: 
    print("wife")
elif "python" in a and "you" not in a: 
    print("python")
elif "shirt" not in a: 
    print("shirt")
elif "need" in a: 
    print("need")
else: print("none")

shirt


#Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result=0
num=1
while num<=1000:
    if num % 3 == 0:
        result += num
    num += 1
    
print(result)
```

