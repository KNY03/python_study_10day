lst = []
num = 0
all_avg =0

while True:
    student_score = []

    student_score.append(input("학번 입력: "))

    if student_score[0].lower() == "exit":
        break

    student_score.append(input("이름 입력: "))
    student_score.append(int(input("국어 점수 입력: ")))
    student_score.append(int(input("영어 점수 입력: ")))
    student_score.append(int(input("수학 점수 입력: ")))

    student_score.append((student_score[2] +
                            student_score[3] +
                            student_score[4]))
    student_score.append(student_score[5] / 3)

    lst.append(student_score)
    print()


print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
print("=========================================================")
print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t")
print("=========================================================")
for i in lst:
    print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f" %
          (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
print("=========================================================")
for item in lst:
    num = len(lst)
    all_avg += item[6]
print("\t\t학생수: %s\t\t\t\t전체 평균 : %.2f" %
      (num, all_avg / num))