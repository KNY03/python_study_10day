# chr(): 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 반환하는 함수
print(chr(97)) # a
print(chr(65)) # A
print(chr(48)) # 0

# dir(): 객체가 지닌 볍수나 함수를 보여주는 함수
print(dir([1, 2, 3]))
print("--------------------------")
print(dir({"1": "a"}))

# enumerate():
for i, name in enumerate(["a", "b", "c"]):
    print(i, name)

print("----------------------------")
for var in enumerate(["a", "b", "c"]):
    print(var)

#################
print()
# map():
def two_times(x):
    return x*2

print(list(map(two_times, [1,2,3])))

###############
print()
# max min
print(max([1, 2, 3]))
print(min([1, 2, 3]))


##############
# ord()
print(ord("a"))
print(ord("A"))
print(ord("0"))

################
# round(): 숫자를 입력받아 반올림해 반환하는 함수
print(round(4.6))
print(round(4.2))
print(round(-4.6))
print(round(-4.2))

##################
# sorted(): 입력 데이터를 정렬한 후 그 결과를 리스트로 반환
print(sorted([3,2,1,]))
print(sorted(["a", "c", "b"]))      # 문자는 유니코드 값으로 순서 정렬
print(sorted("Zero"))
print(sorted([3, 2, 1], reverse=True))

countries = [
    {"code": "kr", "name": "korea"},
    {"code": "CA", "name": "canada"},
    {"code": "US", "name": "united states"},
    {"code": "GB", "name": "united kingdom"},
    {"code": "CN", "name": "china"}
]

print(sorted(countries, key=lambda country: country["code"]))
print(sorted(countries, key=lambda country: country["name"], reverse=True))

my_list = [-5, 3, -1, 0, 2, -4]
print(sorted(my_list, key=abs, reverse=True))

my_list = ["api", "app", "carrier", "demon", "aaa"]
print(sorted(my_list, key=len))

##################################
# sum(): 입력 데이터의 합 반환
print(sum([1, 2, 3]))

###############################
# zip(): 동일한 개수로 이루어진 데이터를 묶어서 반환
print(list(zip([1, 2 ,3 ], [4, 5, 6])))
print(list(zip("abc", "def")))

for i in zip("abc", "def"):
    print(i)

for i in zip("abc", [1, 2, 3]):
    print(i)