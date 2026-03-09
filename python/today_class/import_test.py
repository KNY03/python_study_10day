# module은 각종 함수, 변수, 클래스를 답고 있는 파일이며
# 패키지는 여러 모듈을 묶은 것 이다.

# 모듈은 import를 사용해서 가지고 올 수 있다
import math
print(math.sqrt(4.0))

# as를 사용해서 별칭을 정할 수 있다
import math as m
m.pi
print(m.pi)

# 모듈의 일부만 가지고 올 수 있다.
# 해당 모듈의 모든 기능을 가지고 오고 싶으면 *로 다 불러 올 수 있음
from math import pi # math 모듈에서 변수 pi만 가지고 옴 / 여러개를 가지고 오고 싶으면 , 로 더 지정도 가능함
print(pi)           # 지정을 해주면 굳이 math를 지정하지 않아도 가능함

# 또한 모듈의 일부를 가지고 온 뒤에 이름을 지정하는 것도 가능하다
from math import sqrt as s, pi as p
print(s(4.0))
print(p)

# import로 패키지 가져오기
# import 패키지.모듈
import urllib.request as r           # urllib는 URL처리에 관련된 모듈
response = r.urlopen("http://www.baidu.com")
print(response.status)

# 패키지 설치
# pip install 패키지 로 설치 가능
# 단 인터넷이 필수로 연결되어야함
