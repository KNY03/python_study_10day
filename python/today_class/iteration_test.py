# 이거 파이썬콘솔 에서 실행하기
# it = [1, 2, 3].__iter__()
# it.__next__()
# it.__next__()
# it.__next__()
# it.__next__() # StopIteration 오류 발생

# 문자열, 딕셔너리도 반복자 객체 가능
# 딕셔너리는 뭐를 먼저 가져올지 모름
# set도 마찬가지로 가지고 오는데 순서는 모름

# range를 사용하면 내부적으로 반복자 객체가 만들어 져서 가져온다
it = range(10).__iter__()

# 반복자 객체는 6가지로 리스트, 튜플, range, 문자열, 딕셔너리, 세트

class Counter:
    def __init__(self, stop):
        self.stop = stop
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.stop:
            r = self.count
            self.count += 1
            return r
        else:
            raise StopIteration

for i in range(10):
    print(i, end=" ")

class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, item):
        if item < self.stop:
            return item
        else:
            raise IndexError

print()
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=" ")