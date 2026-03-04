# -*- coding: utf-8 -*-
import csv

fp = open("sangpum_data.csv", "w", encoding="utf-8", newline='') # csv형식으로 저장
wr = csv.writer(fp, delimiter=',', quotechar="'",quoting=csv.QUOTE_ALL)


# w, r, a 모드가 존재함
# b - binary: 이진수 형태로 저장

lst = []
all_sell = 0

while True:
    dct = {}

    dct["code"] = (input("제품코드 입력: "))

    if dct["code"].lower() == "exit":
        break

    dct["name"] = input("제품명 입력: ")
    dct["num"] = int(input("수량 입력: "))
    dct["price"] = int(input("단가 입력: "))

    dct["sell"] = dct["num"] * dct["price"]
    lst.append(dct)

    wr.writerow((dct["code"], dct["name"], dct["num"], dct["price"]))

    print()

fp.close() # 마지막에 꼭 file close를 해야함
