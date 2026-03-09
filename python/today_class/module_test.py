# detetime.data(): 연, 월, 일로 날짜를 표현할 깨 사용
import datetime
print(datetime.datetime.now())
print(datetime.date(2021,3, 21))
day = datetime.date.today()
print(day)
print(day.weekday())

# time.time(): UCT(universal time coordinated, 협정 세계표준)를 사용하며 현제 시간을 출력
# 실수형태로 반환
# 1970년 1웡 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 출력

import time
print(time.time())

# time.localtime(): time.time()을 반환하는 실수값을 연,월,일,시,분,초....
# 형태로 반환
print(time.localtime(time.time()))

# time.strftime(): 시간에 관계된 것을 세밀하게 표현하는 여러가지 포멧 코드를 제공
import time

print(time.strftime("%x", time.localtime(time.time())))
print(time.strftime("%c", time.localtime(time.time())))
print(time.strftime("%Y-%m-%d", time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# datetime class
# 날짜와 시간을 동시에 표현하기 위해 사용됨
# 위에서 다룬 data와 time 클래스에 지우너하는 대부부느이 기능을 지원
from datetime import datetime

now = datetime.now()
print(now)
formatted_date = now.strftime("%Y-%m-%d  %H:%M:%S")
print(formatted_date)
print("%s년 %s월 %s일 %s시 %s분 %s초" % (now.year, now.month, now.day, now.hour, now.minute, now.second))
print(datetime(2026, 3, 8))
print(datetime(2026, 3, 8, 12, 30, 30))

# random 모듈: 난수(규칙 없는 임의의 수)를 발생시킨다
# random 함수: 0 부터 1까지 사이의 랜덤 실수 반환
# uniform 2개의 숫자 사이의 랜덤 실수
# randint 2개의 숫자 사이의 랜덤 실수 - 2번째 인수도 포함
# choice 랜덤하게 하나의 원소 선탹
# sample 랜덤하개 여러개의 원소 선탹
# shuffle 원소의 순서를 랜덤하게

import random
print(random.random())
print("---------------------")
print(random.uniform(1, 10))
print("----------------------")
print(random.randint(1, 10))
print("---------------------")
print(random.randrange(1, 10, 2))
print("---------------------")
print(random.choice("abcdefghij"))
print("---------------------")
print(random.sample([1, 2, 3, 4, 5], 3))
print("---------------------")
i = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(i)
print(i)

# os 모듈: 운영체제에서 제공하는 정보를 제공하거나 운영체제의 기능을 사용할 수 있는 방법을 제공
print()
import os
# print(os.name)
print(os.getcwd())
# print(os.path.join(os.getcwd(), "test"))
# os.mkdir(os.path.join(os.getcwd(), "test")) # 한번만 실행해야함 2번 실행하면 오류남 이미 파일이 생성되었기 때문
# # 파일이 있는지 확인 하려면 os.path.exist
#
# os.rmdir(os.path.join(os.getcwd(), "test"))
# os.remove(os.path.join(os.getcwd(), "test.py")) # 한번만 실행해야함 2번 실행하면 오류남 이미 파일이 생성되었기 때문
#
#
# os.chdir("C:\\Project\\Python_Source\\python311_01\\python\\today_class") # 경로를 변경 하라는 것이고 \\2개를 쓰는 이유는 파이썬에서 \ 표시하기 위해서
# print(os.getcwd())
# print(os.listdir())
# print(os.getcwd())
