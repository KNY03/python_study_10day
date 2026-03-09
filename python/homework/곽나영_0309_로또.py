import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:  # 중복 숫자 뽑기 방지
        result.append(num)

print(sorted(result))  # 무작위 생성된 6개의 숫자 출력
