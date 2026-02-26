# module은 함수를 불러오기 위해서

def hap(a, b):
    return a + b


# 자기 파일만 실행 시킬때 출력이 되도록 함
if __name__ == '__main__': # __ 특정 목적의 변수
    x = 10
    y = 20

    print(hap(x, y))