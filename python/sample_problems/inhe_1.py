class A:                # class A(object) : 여기서 object를 빼도 됨
    def __init__(self, x):
        self.aa = x
    def printA(self):
        print(self.aa)

class B(A):
    def __init__(self, x, y):
        # 부모 클래스 생성자 호출
        super().__init__(x)      # A.__init__(self, x) : A 클래스에 있는 init을 호출     # super(B, self).__init__(x): B 클래스의 부모 클래스의 __init__을 실행하라
        self.bb = y
    def printB(self):
        print(self.bb)

class C(B):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # B.__init__(self, x, y)  # super(C, self).__init__(x, y)
        self.cc = z

    def printC(self):
        print(self.cc)

