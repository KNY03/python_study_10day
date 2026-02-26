# [문제3] 임의의 두수를 입력받아 작은수에서 큰수까지의 구구단을 구해서 출력하시오.

num1 = int(input("첫번째 숫자를 입력하시오 => "))
num2 = int(input("두번째 숫자를 입력하시오 => "))

result = 0

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(" ** %d단 ** " % i, end="\t\t")

    print("")
    for j in range(1, 10):
        for i in range(num1, num2 + 1):
            result = i * j
            print("%d * %d = %2d" % (i, j, result), end="\t\t")
        print("")

else:
    for i in range(num2, num1 + 1):
        print(" ** %d단 ** " % i, end="\t\t")

    print("")
    for j in range(1, 10):
        for i in range(num2, num1 + 1):
            result = i * j
            print("%d * %d = %2d" % (i, j, result), end="\t\t")
        print("")