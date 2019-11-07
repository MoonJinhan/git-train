# x = int(input())
# print(x)

# for c in "string":
#     print(c)

# for i in range(0,5):
#     print(i,i**2)

# score = {
#     '수학' : 80,
#     '국어' : 90,
#     '음악' : 100
# }

# total_score = sum(score.values())
# print(score)
# print(total_score)
# avg = total_score/len(score)
# print(avg)

# 반 평균을 구하세요. 전체 평균

# scores  = {
#     "a" : {
#         "수학": 80,
#         "국어": 90,
#         "음악": 100
#     },
#     "b" : {
#         "수학": 80,
#         "국어": 70,
#         "음악": 80
#     }
# }

# a_sum=sum(scores["a"].values())
# b_sum=sum(scores["b"].values())
# avg = (a_sum + b_sum)/len(scores["a"])
# print(avg)

city = {
    "서울":[-6,-10,5],
    "대전":[-3,-5,2],
    "광주":[0,-2,10],
    "부산":[2,-2,9]
}

# # 3-1 도시별 최근 3일의 온도 평균은?

# city_s = sum(city["서울"])
# print(city_s)

for name,temp in city.items():
    avg_temp = sum(temp)/len(temp)
    print(f'{name} : 평균기온은 {avg_temp} 입니다.')


# 3-2 위에서 서울은 영상 2도였던 적이 있나요?>

# A if 조건문 else B : 조건문이 참이면 A 거짓이면 B

print("있어요") if 2 in city["대전"] else print("없어요")