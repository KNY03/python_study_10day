# 2026.02.25

list = []

code = (input("제품코드 입력: "))
list.append(code)
# list.append(input("제품코드 입력: "))

name = input("제품명 입력: ")
list.append(name)

num = int(input("수량 입력: "))
list.append(num)

price = int(input("단가 입력: "))
list.append(price)


sell = num * price
list.append(sell)
#list.append(list[2] * list[3])

print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
print("================================================")
print("  %4s \t %8s \t %3d \t %3d \t %6d" %(list[0], list[1], list[2], list[3], list[4]))
# print("  %4s \t %8s \t %3d \t %3d \t %6d" %(list.pop(0), list.pop(0), list.pop(0), list.pop(0), list.pop(0)))
print("================================================")
