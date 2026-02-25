#2026.02.25

list = []

list.append(input("Input student number: "))
list.append(input("Input student name: "))
list.append(int(input("Input student korean score: ")))
list.append(int(input("Input student english score: ")))
list.append(int(input("Input student math score: ")))

list.append(list[2] + list[3] + list[4])
list.append((list[2] + list[3] + list[3]) / 3)

print("\t\t\t\t\t\t***성적표***\t\t\t\t\t\t")
print("=========================================================")
print("\t학번\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균\t")
print("=========================================================")
print("  %4s  %6s  %4d  %6d  %6d   %6d   %6.2f" %
      (list[0], list[1], list[2], list[3], list[4], list[5], list[6]))
print("=========================================================")

