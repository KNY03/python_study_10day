#2026.02.25

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


print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
print("=========================================================")
print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t")
print("=========================================================")
#
# print(f"\t{student_score['student_num']}\t"
#       f"{student_score['student_name']}\t"
#       f"{student_score['student_kor']}\t\t"
#       f"{student_score['student_eng']}\t\t"
#       f"{student_score['student_math']}\t\t"
#       f"{student_score['total_score']}\t\t"
#       f"{student_score['avg']:.2f}")

print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f" %
      (student_score["student_num"],
       student_score["student_name"],
       student_score["student_kor"],
       student_score["student_eng"],
       student_score["student_math"],
       student_score["total_score"],
       student_score["avg"]))
print("=========================================================")