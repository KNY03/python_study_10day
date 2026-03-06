class A:                # class A(object) : 여기서 object를 빼도 됨
    def __init__(self):
        self.aa = 10
    def printA(self):
        print(self.aa)

class B(A):
    def __init__(self):
        # 부모 클래스 생성자 호출
        super().__init__()      # A.__init__(self) : A 클래스에 있는 init을 호출     # super(B, self).__init__(): B 클래스의 부모 클래스의 __init__()을 실행하라
        self.bb = 20
    def printB(self):
        print(self.bb)

class C(B):
    def __init__(self):
        super().__init__()  # B.__init__(self)  # super(C, self).__init__()
        self.cc = 30

    def printC(self):
        print(self.cc)

