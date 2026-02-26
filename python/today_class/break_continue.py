# 2중 for문에서 break를 만나면 안에있는 for문민 빠져나간다



# 홀수만 출력함
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)