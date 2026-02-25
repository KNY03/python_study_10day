# 1 ~ 100까지 짝수 합, 홀수 합 구하기
# ver 1
total_even = 0
total_odd = 0

for i in range(0, 101, 2):
    total_even += i

print(f"짝수의 합은 {total_even}입니다.")

for i in range(1, 101, 2):
    total_odd += i

print(f"홀수의 합은 {total_odd}입니다.")


############################################
# ver 2
total_even = 0
total_odd = 0

for i in range(0, 101):
    if i % 2 == 0:
        total_even += i
    else:
        total_odd += i

print(f"짝수의 합은 {total_even}입니다.")
print(f"홀수의 합은 {total_odd}입니다.")