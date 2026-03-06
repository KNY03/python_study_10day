from inhe_1 import *

if __name__ == "__main__":
    obj = C(100, 200, 300)       # C는 모든 객체를 상속 받았기 때문에 다 사용이 가능하디
    print(obj.cc)
    print(obj.bb)
    print(obj.aa)
    print()
    obj.printA()
    obj.printB()
    obj.printC()