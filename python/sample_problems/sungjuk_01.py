#2026.02.25

student_num = (input("Input student number: "))
student_name = (input("Input student name: "))
student_kor = int(input("Input student korean score: "))
student_eng = int(input("Input student english score: "))
student_math = int(input("Input student math score: "))

total_score = student_kor + student_eng + student_math

avg = (student_kor + student_eng + student_math) / 3

print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
print("=========================================================")
print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t")
print("=========================================================")
print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f" %
      (student_num, student_name, student_kor, student_eng, student_math, total_score, avg))
print("=========================================================")

