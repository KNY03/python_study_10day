dct = ({})

dct["code"] = (input("제품코드 입력: "))
dct["name"]  = input("제품명 입력: ")
dct["num"]  = int(input("수량 입력: "))
dct["price"]  = int(input("단가 입력: "))

dct["sell"] = dct["num"] * dct["price"]

print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
print("================================================")
print("  %4s \t %8s \t %3d \t %3d \t %6d" %(dct["code"], dct["name"], dct["num"],dct["price"], dct["sell"]))
print("================================================")