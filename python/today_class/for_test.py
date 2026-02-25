total = 0

for i in range(1,11):
    total = total + i

print("1부터 10까지의 합은", total,"입니다.")
# print(f"1부터 10까지의 합은{total}입니다".)

################################################

message = "Hello!"
messages = ["Hello World!" , "강릉원주대학교 정보기술공학과"]
numbers = (1, 2, 3, 4)
polygon = {"triangle": 2, "rectangle": 3, "circle": 4, "line": 0}
color = {"red", "green", "blue"} # set 객체

for i in message:
    print(i)
print("======================")

for i in messages:
    print(i)
print("======================")

for i in numbers:
    print(i)
print("======================")

for i in polygon:
    print(i)
    print(polygon[i]) # print(polygon.get(i))
    # method는 함수라 ()를 사용함.
print("======================")

for i in color:
    print(i)
print("======================")

############################################################
#for문과 else / break 

total = 0
for i in range(1,101, 1):
    if i == 10:
        total = total + i
    else:
        print("1부터 10까지의 합은", total,"입니다.")
        break

###########################################################
# list - for

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0] # 참이여야만 리스트에 포함됨
print(result)