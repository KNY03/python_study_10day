score = int(input("총점을 입력하시오: "))

if score >= 90:
    print("수")
elif score >= 80:
    print("우")
elif score >= 70:
    print("미")
elif score >= 60:
    print("양")
else:
    print("가")

# elif 앞에는 else가 올 수 없다.

print("The End.....")