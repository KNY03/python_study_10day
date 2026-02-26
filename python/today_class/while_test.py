"""
1. 초기식: i = 0 (반복문에는 꼭 필요함)
2. 조건식: while i < 100
3. 반복처리할 내용: print()
4. 증감식: i ++
"""

# import random   # random 모듈을 가져옴
from random import randint

i = 0
while i != 3:
    # i = random.randint(1, 6)
    i = randint(1,6)
    print(i)

