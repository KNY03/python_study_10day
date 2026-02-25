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

# 등급 관리
if student_score["avg"]  >= 90:
    student_score["grade"] = "수"
elif student_score["avg"]  >= 80:
    student_score["grade"] = "우"
elif student_score["avg"]  >= 70:
    student_score["grade"] = "미"
elif student_score["avg"]  >= 60:
    student_score["grade"] = "양"
else:
    student_score["grade"] = "가"

# 출력 화면
print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
print("======================================================================")
print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t\t등급")
print("======================================================================")


print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f  %4s" %
      (student_score["student_num"],
       student_score["student_name"],
       student_score["student_kor"],
       student_score["student_eng"],
       student_score["student_math"],
       student_score["total_score"],
       student_score["avg"],
       student_score["grade"]))

print("======================================================================")