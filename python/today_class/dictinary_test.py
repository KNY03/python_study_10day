lux = dict({"health" : 499, "mana" : 344, "melee": 550, "armor": 18.72}) #dict를 적지 않아도 동작이 된다.
print(lux)
print((lux["health"]))
print((lux["mana"]))

lux2 = dict(zip(["health", "mana", "melee", "armor"], [500, 240, 600, 20.78]))
print(lux2)
print((lux2["health"]))
print((lux2["mana"]))

lux3 = dict([("health", 400),("mana", 300),("melee", 200),("armor", 100)])
print(lux3)
print((lux3["health"]))
print((lux3["mana"]))

lux4 = dict(health = 300, mana = 400, melee = 200, armor = 100)
print(lux4)
print((lux4["health"]))
print((lux4["mana"]))

# 키 값이 있으면 수정, 없으면 추가

# 관련함수
"""
values(): 키를 리스트 형태로 반환 - key return
keys(): 값을 리스트 형태로 반환 - value return
items(): 키와 값을 튜플로 만들어 리스트 형식으로 반환  - key, value 둘다 return
## 위 3개는 꼭 기억!!!

clear(): 모든 요소 삭제
get(): 키와 대응되는 값을 반환
in: 해당 키의 존재 여부(True or False)
"""
####################################################################3
dct = {}
dct["id"] = "hong"
dct["pw"] = "1234"
dct["email"] = "hong@gmail.com"

print(dct)
print(dct.keys())
print(dct.values())
print(dct.items())

res = dct.get("id") # dcr["id"]
print(res)
print(dct.pop("pw")) # list, dic 둘다 사용가능 / 값이 없으면 0으로 반환
print(dct)

dct.clear()
print(dct)

#################################################################
x = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}
for i in x:  # key만 출력
    print(i)

for key, value in x.items(): # key value 출력
    print(key, value)

##########################################################

import copy

x = {"python" : {"version": "2.7"}, "script" : {"name": "hello.py"}}
a = x
b = x.copy()
x["python"]["version"] = "3.7"

print(b["python"]["version"])
