#2026.03.04
import csv
import os

def menu_title():
    print("\n*** 성적관리 ***")
    print("1. 성적정보 입력: ")
    print("2. 성적정보 출력: ")
    print("3. 성적정보 조회: ")
    print("4. 성적정보 수정: ")
    print("5. 성적정보 삭제: ")
    print("6. 프로그램 종료: ")
    print()

def check_grade(x):
    if x >= 90:
        score = "수"
    elif x >= 80:
        score = "우"
    elif x >= 70:
        score = "미"
    elif x >= 60:
        score = "양"
    else:
        score = "가"
    return score

def input_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open("sungjuk_data.csv", "at", encoding="utf-8", newline='')
        fieldnames = ["student_num", "student_name", "student_kor", "student_eng", "student_math", "total_score", "avg", "grade"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)

    else:
        fp = open("sungjuk_data.csv", "at", encoding="utf-8", newline='')
        fieldnames = ["student_num", "student_name", "student_kor", "student_eng", "student_math", "total_score", "avg", "grade"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        wr.writeheader()

    student_score = {}
    student_score["student_num"] = input("학번 입력: ")
    student_score["student_name"] = input("이름 입력: ")

    student_score["student_kor"] = int(input("국어 점수 입력: "))
    student_score["student_eng"] = int(input("영어 점수 입력: "))
    student_score["student_math"] = int(input("수학 점수 입력: "))

    total = (student_score["student_kor"] +
             student_score["student_eng"] +
             student_score["student_math"])

    student_score["total_score"] = total
    student_score["avg"] = total / 3

    x = check_grade(student_score["avg"])
    student_score["grade"] = x

    wr.writerow(student_score)

    fp.close()
    print("\n데이터를 추가하였습니다!\n")

def print_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open("sungjuk_data.csv", "r", encoding="utf-8", newline='')
        rd = list(csv.DictReader(fp))
        std_num = 0
        total = 0

        print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
        print("======================================================================")
        print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t\t등급")
        print("======================================================================")
        for data in rd:
            x = check_grade(float(data["avg"]))
            data["grade"] = x
            std_num += 1
            total += float(data["avg"])
            print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f  %4s" %
                  (data["student_num"],
                   data["student_name"],
                   int(data["student_kor"]),
                   int(data["student_eng"]),
                   int(data["student_math"]),
                   int(data["total_score"]),
                   float(data["avg"]),
                   data["grade"]))
        print("======================================================================")
        print("\t\t\t\t\t 총 학생수: %d\t\t 평균 성적: %.2f" % (std_num, total/std_num))
    else:
        print("\n출력할 정보가 없음!!!")

def search_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open("sungjuk_data.csv", "r", encoding="utf-8", newline='')
        rd = list(csv.DictReader(fp))
        data_num = (input("찾고싶은 학생번호를 입력하시오: "))
        found = False

        for data in rd:
            if data_num == data["student_num"]:
                x = check_grade(float(data["avg"]))
                data["grade"] = x

                print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t\t등급")
                print("======================================================================")
                print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f  %4s" %
                      (data["student_num"],
                       data["student_name"],
                       int(data["student_kor"]),
                       int(data["student_eng"]),
                       int(data["student_math"]),
                       int(data["total_score"]),
                       float(data["avg"]),
                       data["grade"]))
                print("======================================================================")
                print()
                found = True
                break  # 동일한 코드가 있으면 여러개 출력

        if not found:
            print("\n해당 학생은 없습니다.\n")

def update_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open("sungjuk_data.csv", "r", encoding="utf-8", newline='')
        lst = list(csv.DictReader(fp))
        data_num = (input("수정하고 싶은 학생 번호를 입력하시오: "))
        found = False

        for data in lst:
            if data_num == data["student_num"]:
                print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
                print("======================================================================")
                print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t\t등급")
                print("======================================================================")
                data["student_name"] = (input("이름을 다시 작성해 주세요: "))
                data["student_kor"] = int(input("국어 점수를 다시 입력해 주세요: "))
                data["student_eng"] = int(input("수학 점수를 다시 입력해 주세요: "))
                data["student_math"] = int(input("영어 점수를 다시 입력해 주세요: "))
                total = (data["student_kor"] +
                         data["student_eng"] +
                         data["student_math"])

                data["total_score"] = total
                data["avg"] = total / 3
                x = check_grade(float(data["avg"]))
                data["grade"] = x
                print("====================================================")
                print()
                found = True
                break  # 동일한 코드가 있으면 여러개 출력

        if not found:
             print("\n해당 학생은 없습니다.\n")

        fp.close()

        if found:
            fp2 = open("sungjuk_data.csv", "w", encoding="utf-8", newline='')
            fieldnames = ["student_num", "student_name", "student_kor", "student_eng", "student_math", "total_score", "avg", "grade"]
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)
            fp2.close()
        else:
            print("\n해당 학생은 없습니다.\n")

def delete_sungjuk():
    if os.path.exists('sungjuk_data.csv'):
        fp = open("sungjuk_data.csv", "r", encoding="utf-8", newline='')
        lst = list(csv.DictReader(fp))
        data_num = (input("삭제하고 싶은 학생 번호를 입력하시오: "))
        found = False

        for data in lst:
            if data_num == data["student_num"]:
                print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t\t등급")
                print("======================================================================")
                print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f  %4s" %
                      (data["student_num"],
                       data["student_name"],
                       int(data["student_kor"]),
                       int(data["student_eng"]),
                       int(data["student_math"]),
                       int(data["total_score"]),
                       float(data["avg"]),
                       data["grade"]))
                print("\n====================================================")
                lst.remove(data)

                print("삭제되었습니다")
                print("====================================================")
                print()
                found = True
                break  # 동일한 코드가 있으면 여러개 출력

        if not found:
            print("\n해당 학생은 없습니다.\n")

        fp.close()

        if found:
            fp2 = open("sungjuk_data.csv", "w", encoding="utf-8", newline='')
            fieldnames = ["student_num", "student_name", "student_kor", "student_eng", "student_math", "total_score",
                          "avg", "grade"]
            wr = csv.DictWriter(fp2, fieldnames=fieldnames)
            wr.writeheader()
            wr.writerows(lst)

            fp2.close()
        else:
            print("\n해당 학생은 없습니다.\n")

if __name__ == "__main__":
    while True:
        menu_title()
        menu = int(input("\n메뉴를 선택하시오(1~6): "))
        print()
        if menu == 1:
            input_sungjuk()
        elif menu == 2:
            print_sungjuk()
        elif menu == 3:
            search_sungjuk()
        elif menu == 4:
            update_sungjuk()
        elif menu == 5:
            delete_sungjuk()
        elif menu == 6:
            print("\n프로그램을 종료합니다!")
            break
        else:
            print("\n메뉴를 다시 입력하시오!\n")

