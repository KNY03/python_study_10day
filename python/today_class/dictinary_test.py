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
values(): 키를 리스트 형태로 반환
keys(): 값을 리스트 형태로 반환
items(): 키와 값을 튜플로 만들어 리스트 형식으로 반환 
clear(): 모든 요소 삭제
get(): 키와 대응되는 값을 반환
in: 해당 키의 존재 여부(True or False)
"""