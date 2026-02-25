#[문제1] 임의의 수를 입력받아 해당 숫자의 국단을 출력하시오.
dan = int(input("단을 입력하시오 => "))

result = 0
print(" ** 5단 ** ")
for i in range(1, 10):
    result = dan * i
    print("%d * %d = %2d" % (dan, i, result))