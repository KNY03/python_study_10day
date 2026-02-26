a = set("apple") # 유일한 문자만 세트로 출력
print(a)

# 인덱스는 사용불가
# 비순차 구조

#####################################

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b)) # or set.difference(a,b)
print(a.union(b))
# ....

######################################

c = {1, 2, 3, 4}
d = {3, 4, 5, 6}

c.remove(1) # 값이 없으면 오류 - discard(요소) : 삭제의 개념 - 여기서는 값이 없으면 넘어감
print(c)

#######################################

a.clear()
b.clear()

a = {1, 2, 3, 4}
b = a               # 같은 객체 주소를 씀

print(b)
print(a)

a.add(10)
print(a)
print(b)

#######################################

a.clear()
b.clear()

a = {1, 2, 3, 4}
b = a.copy()              # copy를 하면 다른 객체로 저장되기 때문에 수정이 안됨

print(b)
print(a)

a.add(10)
print(a)
print(b)