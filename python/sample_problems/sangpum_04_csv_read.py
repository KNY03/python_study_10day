# -*- coding: utf-8 -*-
import csv
import os

fp = open("sangpum_data.csv", "r", encoding="utf-8", newline='') # csv형식으로 저장


if os.path.exists('sangpum_data.csv'): # 읽기 모드에서는 파일의 유무가 중요하다
    fp = open("sangpum_data.csv", "r", encoding="utf-8")
    reader = list(csv.reader(fp))

    lst = []
    for line in reader:
        dct = {}
        dct["code"] = line[0]
        dct["name"] = line[1]
        dct["num"] = line[2]
        dct["price"] = line[3]

        lst.append(dct)

    print("\n=============== 📦 상품 판매 현황 ====================")
    print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
    print("====================================================")
    print("====================================================")
    all_sell = 0
    for dct in lst:
        sales = int(dct["num"].strip("'")) * int(dct["price"].strip("'"))
        all_sell += sales
        print(
            "  %4s \t %6s \t %3s \t %3s \t %3d" %
            (dct["code"], dct["name"], (dct["num"]), (dct["price"]), sales))

    print("====================================================")
    print("                   < 총 판매 금액 >")
    print("총 판매 금액은: %30d" % all_sell)
    print("====================================================")
    print("====================================================")
    print("                   ✔ 출력 완료 ✔")
    print("====================================================")

else:
    print("해당 파일이 없습니다!!")


fp.close()


