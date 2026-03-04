# -*- coding: utf-8 -*-
import csv
import os

lst = []
all_sell = 0

def input_data():
    fp = open("sangpum_data_02.csv", "at", encoding="utf-8", newline='')  # csv형식으로 저장
    wr = csv.writer(fp, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL)

    dct = {}

    dct["code"] = (input("제품코드 입력: ")).strip()
    dct["name"] = input("제품명 입력: ").strip()
    dct["num"] = (input("수량 입력: ")).strip()
    dct["price"] = (input("단가 입력: ")).strip()

    dct["sell"] = int(dct["num"]) * int(dct["price"])
    wr.writerow((dct["code"], dct["name"], dct["num"], dct["price"], dct["sell"]))

    fp.close()
    print("\n데이터를 추가하였습니다!\n")

def print_data():
    if os.path.exists('sangpum_data_02.csv'):
        global all_sell
        fp = open("sangpum_data_02.csv", "r", encoding="utf-8", newline='')
        rd = csv.reader(fp, delimiter=',', quotechar="'")
        lst = list(rd)

        print("\n=============== 📦 상품 판매 현황 ====================")
        print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
        print("====================================================")
        print("====================================================")
        all_sell = 0
        for data in lst:
            all_sell += int(data[4].strip("'"))
            print(
                "  %4s \t %6s \t %3d \t %3d \t %3d" %
                (data[0], data[1], int(data[2]), int(data[3]), int(data[4])))

        print("====================================================")
        print("                   < 총 판매 금액 >")
        print("총 판매 금액은: %30d" % all_sell)
        print("====================================================")
        print("====================================================")
        print("                   ✔ 출력 완료 ✔")
        print("====================================================")
    else:
        print("\n출력할 정보가 없음!!!")


if __name__ == "__main__":
    while True:
        menu = int(input("\n메뉴를 선택하시오(1~3): "))
        if menu == 1:
            input_data()
        elif menu == 2:
            print_data()
        elif menu == 3:
            print("\n프로그램을 종료합니다!")
            break
        else:
            print("\n메뉴를 다시 입력하시오!\n")



