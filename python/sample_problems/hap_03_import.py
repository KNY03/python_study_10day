# hap_02_module.py 파일에 있는 함수를 import 하기 위해 만들어짐

import hap_02_module

def div(a, b):
    return a / b


if __name__ == '__main__': # __ 특정 목적의 변수
    print(hap_02_module.hap(100, 200))
    print(div(10, 2))


