from inhe import *

if __name__ == "__main__":
    obj = C()       # C는 모든 객체를 상속 받았기 때문에 다 사용이 가능하디
    print(obj.cc)
    print(obj.bb)
    print(obj.aa)
    print()
    obj.printA()
    obj.printB()
    obj.printC()