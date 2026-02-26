#########################################
# ver 1
even = 0
odd = 0

while True:
    for i in range(1, 101):
        if i % 2 == 0:
            even = i + even
        else:
            odd = i + odd
    print(even)
    print(odd)
    break

######################################
# ver 2
even = 0
odd = 0
j = 1 # 초기식

while j < 101: # 조건식

    # 반복처리할 내용
    if j % 2 == 0:
        even = even + j
    else:
        odd = odd + j

    j += 1 # 증감식

else: # while else 사용 가능함. 단 break를 먼저 만나면 else는 실핼리 안됨
    print(even)
    print(odd)

#########################################
# ver 3
even = 0
odd = 0
i = 0

while True:
    if i % 2 == 0:
        even = i + even
    else:
        odd = i + odd
    i += 1

    if i > 100:
        print(even)
        print(odd)
        break