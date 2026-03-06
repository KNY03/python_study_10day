import abc


class Person:
    def __init__(self, name, age, address):
        self.hello = "Hello"
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다. '.format(self.hello, self.name))

james = Person('마리아', 20, '서울시 서초구')
james.greeting()

print('이름: ', james.name)
print('나이: ', james.age)
print('주소: ', james.address)

"""
접근 제한자
- 파이썬은 자바나 C++처럼 명시적으로 public, protected, private와 같은 키워드를 사용하지 않는 대신 밑줄(_) 를 사용해서 접근제한을 구분한다.
- 밑줄이 없는 경우 public처럼 객체 생성 후 누구나 외부에서 직접 접근이 가능하다.
- 밑줄이 하나인 경우 비공개모드로서 직접적인 접근을 제한하고 있고 객체 생성 후 외부에서 직접적인 접근을 해서는 안된다. 하지만 접근을 시도하면 오류없이 접근은 가능하다.
- 밑줄이 두개인 경우는 객체 생성 후 외부에서 직접적인 접근을 할 수 없으며 객체 생성 후 직접 접근을 시도하면 정의되지 않은 속성이나 메소드 라고 오류 메시지가 발생한다.
- 밑줄이 두개인 경우 객체 내부에서는 접근이 가능하며 자식 틀래스에세 상속도지 않는다. 
"""

class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = "Hello"
        self._name = name
        self._age = age
        self._address = address
        self.__wallet = wallet

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_wallet(self):
        return self.__wallet
    def set_wallet(self, wallet):
        self.__wallet = wallet

    name=property(get_name, set_name)
    age = property(get_age, set_age)
    address = property(get_address, set_address)
    wallet = property(get_wallet, set_wallet)

    def pay(self, amount):
        self.__wallet -= amount
        print("이제 {0}원 남았음".format(self.__wallet))

if __name__ == '__main__':
    james = Person('마리아', 20, '서울시 서초구', 10000)
    print(james.name)
    james.name = "anan"
    print(james.name)
    james.pay(100)


##########################################################
# 클래스 상속
class Person:
    def greeting(self):
        print("Hello!!")

class Student(Person):  # 지금은 단일 상속이지만 파이썬은 다중상속이 가능하다
    def study(self):
        print("공부하기")

james = Student()
james.greeting()
james.study()


class Person:
    def greeting(self):
        print("Hello!!")

class PersonList:
        def __init__(self):
            self.person_list = []

        def append_person(self, person):
            self.person_list.append(person)

if __name__ == '__main__':
    person = Person()
    person.greeting()
    pl = PersonList()
    pl.append_person(person)
    print(pl.person_list)
    pl.person_list[0].greeting()

###############################################
# 기반 클래스의 상속
class Person:
    def __init__(self):
        print('person __init__')
        self.hello = "Hello"

class Student(Person):
    def __init__(self):
        super().__init__()  # 이게 있으면 밑에 오류가 없음
        print('student __init__')
        self.school = "python coding stamp"

james = Student()
print(james.school)
print(james.hello)  # 에러 발생
# 파이썬은 안됨
# 기반클래스를 호출하지 않음

print()
class Person:
    def __init__(self):
        print('person __init__')
        self.hello = "Hello"

class Student(Person):
    pass

james = Student()
print(james.hello)

#################################################
# 다중 상속
print()
class Person:
    def __init__(self):
        print('person __init__')
    def greeting(self):
        print("Hello!!")

class University:
    def __init__(self):
        print('university __init__')
    def manage_credit(self):
        print("학점 관리")
    def greeting(self):
        print("Hi")

class Undergraduate(Person, University):
    def study(self):
        print("공부하기")

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()

###################################################
# 다이아몬드 상속
# 잘못된 상속이다.
# 사용하지 않는 편이 좋음
print()
class A:
    def greeting(self):
        print("A")

class B(A):
    def greeting(self):
        print("B")

class C(A):
    def greeting(self):
        print("C")

class D(B,C):
    pass


x = D()
x.greeting()



################################################
# 추상 클래스
"""
자식 클래스가 반드시 구현하도록 강제하기 위해

공통 인터페이스(형식)를 만들기 위해

코드 구조를 통일하기 위해
"""

print()
from abc import *

class StudentBase(metaclass=abc.ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print("study!!")

    def go_to_school(self):
        print("go to school!!")

class Student2(StudentBase):
    def study(self):
        print("playing game!!")

    def go_to_school(self):
        print("Student2 go to playground!!")

    def sleep(self):
        print("sleep!!")

james = Student()
james.study()
james.go_to_school()
print("---")
mian = Student2()
mian.study()
mian.go_to_school()
mian.sleep()
print("---")
lst = []
lst.append(james)
lst.append(mian)
for item in lst:
    item.study()
    item.go_to_school()
    print("---")

