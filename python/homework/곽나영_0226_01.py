lst = []
num = 0
all_avg =0

while True:
    student_score = {}

    student_score["student_num"] = input("학번 입력: ")

    if student_score["student_num"].lower() == "exit":
        break

    student_score["student_name"] = input("이름 입력: ")
    student_score["student_kor"] = int(input("국어 점수 입력: "))
    student_score["student_eng"] = int(input("영어 점수 입력: "))
    student_score["student_math"] = int(input("수학 점수 입력: "))

    student_score["total_score"] = (student_score["student_kor"] +
                                    student_score["student_eng"] +
                                    student_score["student_math"])
    student_score["avg"] = student_score["total_score"] / 3

    lst.append(student_score)
    print()


print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
print("=========================================================")
print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t")
print("=========================================================")
for dct in lst:
    print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f" %
          (dct["student_num"],
           dct["student_name"],
           dct["student_kor"],
           dct["student_eng"],
           dct["student_math"],
           dct["total_score"],
           dct["avg"]))
print("=========================================================")
for item in lst:
    num = len(lst)
    all_avg += item["avg"]
print("\t\t학생수: %s\t\t\t\t전체 평균 : %.2f" %
      (num, all_avg / num))