# -*- coding: utf-8 -*-
import csv
import os
from os import remove

lst = []
all_sell = 0

def menu_title():
    print("\n======= 제품 관리 ========")
    print("1. 제품정보 입력: ")
    print("2. 제품정보 출력: ")
    print("3. 제품정보 조회: ")
    print("4. 제품정보 수정: ")
    print("5. 제품정보 삭제: ")
    print("6. 프로그램 종료: ")
    print("====================\n")

def input_data():
    if os.path.exists('sangpum_data_03.csv'):
        fp = open("sangpum_data_03.csv", "at", encoding="utf-8", newline='')  # csv형식으로 저장
        fieldnames = ["code", "name", "num", "price", "sell"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)

    else:
        fp = open("sangpum_data_03.csv", "at", encoding="utf-8", newline='')
        fieldnames = ["code", "name", "num", "price", "sell"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()


    dct = {}

    dct["code"] = (input("제품코드 입력: "))
    dct["name"] = input("제품명 입력: ")
    dct["num"] = (input("수량 입력: "))
    dct["price"] = (input("단가 입력: "))

    dct["sell"] = int(dct["num"]) * int(dct["price"])
    wr.writerow(dct)

    fp.close()
    print("\n데이터를 추가하였습니다!\n")

def print_data():
    if os.path.exists('sangpum_data_03.csv'):
        global all_sell
        fp = open("sangpum_data_03.csv", "r", encoding="utf-8", newline='')
        rd = list(csv.DictReader(fp))
        # lst = list(rd)

        print("\n=============== 📦 상품 판매 현황 ====================")
        print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
        print("====================================================")
        print("====================================================")
        all_sell = 0
        for data in rd:
            all_sell += int(data["sell"])
            print(
                "  %4s \t %6s \t %3d \t %3d \t %3d" %
                (data["code"], data["name"], int(data["num"]), int(data["price"]), int(data["sell"])))

        print("====================================================")
        print("                   < 총 판매 금액 >")
        print("총 판매 금액은: %30d" % all_sell)
        print("====================================================")
        print("====================================================")
        print("                   ✔ 출력 완료 ✔")
        print("====================================================")
    else:
        print("\n출력할 정보가 없음!!!")

def search_data():
    if os.path.exists('sangpum_data_03.csv'):
        fp = open("sangpum_data_03.csv", "r", encoding="utf-8", newline='')
        rd = list(csv.DictReader(fp))
        data_num = (input("찾고싶은 데이터의 제품번호를 입력하시오: "))
        found = False

        for data in rd:
            if data_num == data["code"]:
                print("\n====================================================")
                print("  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
                print(
                    "  %4s \t %6s \t %3d \t %3d \t %3d" %
                    (data["code"], data["name"], int(data["num"]), int(data["price"]), int(data["sell"])))
                print("====================================================")
                print()
                found = True
                break       # 동일한 코드가 있으면 여러개 출력

        if not found:
            print("\n해당 제품은 없습니다.\n")


def update_data():
    if os.path.exists('sangpum_data_03.csv'):
        fp = open("sangpum_data_03.csv", "r", encoding="utf-8", newline='')
        lst = list(csv.DictReader(fp))
        data_num = (input("수정하고 싶은 데이터의 제품번호를 입력하시오: "))
        found = False

        for data in lst:
            if data_num == data["code"]:
                print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
                print(
                    "  %4s \t %6s \t %3d \t %3d \t %3d" %
                    (data["code"], data["name"], int(data["num"]), int(data["price"]), int(data["sell"])))
                print("\n====================================================")
                data["num"] = int(input("수량을 다시 작성해 주세요: "))
                data["price"] = int(input("단가를 다시 입력해 주세요: "))
                data["sell"] = data["num"] * data["price"]
                print("====================================================")
                print()
                found = True
                break  # 동일한 코드가 있으면 여러개 출력

        if not found:
             print("\n해당 제품은 없습니다.\n")

        fp.close()

        if found:
            fp2 = open("sangpum_data_03.csv", "w", encoding="utf-8", newline='')
            fieldnames = ["code", "name", "num", "price", "sell"]
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)
            fp2.close()
        else:
            print("\n해당 제품은 없습니다.\n")

def delete_data():
    if os.path.exists('sangpum_data_03.csv'):
        fp = open("sangpum_data_03.csv", "r", encoding="utf-8", newline='')
        lst = list(csv.DictReader(fp))
        data_num = (input("삭제하고 싶은 데이터의 제품번호를 입력하시오: "))
        found = False

        for data in lst:
            if data_num == data["code"]:
                print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
                print(
                    "  %4s \t %6s \t %3d \t %3d \t %3d" %
                    (data["code"], data["name"], int(data["num"]), int(data["price"]), int(data["sell"])))
                print("\n====================================================")
                # del data["code"], data["name"], data["num"], data["price"], data["sell"]
                lst.remove(data)

                print("삭제되었습니다")
                print("====================================================")
                print()
                found = True
                break  # 동일한 코드가 있으면 여러개 출력

        if not found:
            print("\n해당 제품은 없습니다.\n")

        fp.close()

        if found:
            fp2 = open("sangpum_data_03.csv", "w", encoding="utf-8", newline='')
            fieldnames = ["code", "name", "num", "price", "sell"]
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)

            fp2.close()
        else:
            print("\n해당 제품은 없습니다.\n")


if __name__ == "__main__":
    while True:
        menu_title()
        menu = int(input("\n메뉴를 선택하시오(1~6): "))
        if menu == 1:
            input_data()
        elif menu == 2:
            print_data()
        elif menu == 3:
            search_data()
        elif menu == 4:
            update_data()
        elif menu == 5:
            delete_data()
        elif menu == 6:
            print("\n프로그램을 종료합니다!")
            break
        else:
            print("\n메뉴를 다시 입력하시오!\n")

