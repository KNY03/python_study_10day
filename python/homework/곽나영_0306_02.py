class NoInput(Exception):
  def __init__(self):
    super().__init__("아무것도 입력하지 않았습니다.")

class BetweenNumException(Exception):
  def __init__(self):
    super().__init__("0 ~ 100 사이의 수를 입력해 주세요")

class SameKeyException(Exception):
  def __init__(self):
    super().__init__("동일한 학번이 있습니다. 다시 입력해 주새요.")



class Sungjuk:
  def __init__(self):
    self._hakbun = ""
    self._irum = ""
    self._kor = 0
    self._eng = 0
    self._math = 0
    self._tot = 0
    self._avg = 0.0
    self._grade = ""

  def get_hakbun(self):
    return self._hakbun
  def set_hakbun(self, hakbun):
    self._hakbun = hakbun
  hakbun = property(get_hakbun, set_hakbun)

  def get_irum(self):
    return self._irum
  def set_irum(self, irum):
    self._irum = irum
  irum = property(get_irum, set_irum)

  def get_kor(self):
    return self._kor
  def set_kor(self, kor):
    self._kor = kor
  kor = property(get_kor, set_kor)

  def get_eng(self):
    return self._eng
  def set_eng(self, eng):
    self._eng = eng
  eng = property(get_eng, set_eng)

  def get_math(self):
    return self._math
  def set_math(self, math):
    self._math = math
  math = property(get_math, set_math)

  def get_tot(self):
    return self._tot
  def set_tot(self, tot):
    self._tot = tot
  tot = property(get_tot, set_tot)

  def get_avg(self):
    return self._avg
  def set_avg(self, avg):
    self._avg = avg
  avg = property(get_avg, set_avg)

  def get_grade(self):
    return self._grade
  def set_grade(self, grade):
    self._grade = grade
  grade = property(get_grade, set_grade)

  def input_sungjuk(self, lst):  ## 동일한 이름을 넣을 경우
    while True:
      try:
        self._hakbun = input("학번 입력 => ")
        for obj in lst:
          if self._hakbun == obj.hakbun:
            raise SameKeyException()
          elif self._hakbun.strip() == "":
            raise NoInput()
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break

    while True:
      try:
        self._irum = input("이름 입력 => ")
        if self._irum.strip() == "": # 좀더 고민
          raise NoInput()
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break

    self.update_sungjuk()

  def update_sungjuk(self):
    while True:
      try:
        self._kor = int(input("국어 점수 입력 => "))
        if self._kor < 0 or self._kor > 100:
          raise BetweenNumException()
      except ValueError as e:
        print("숫자를 입력해 주세요(%s)\n" % e)
        print()
        continue
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break

    while True:
      try:
        self._eng = int(input("영어 점수 입력 => "))
        if self._eng < 0 or self._eng > 100:
          raise BetweenNumException()
      except ValueError as e:
        print("숫자를 입력해 주세요(%s)\n" % e)
        print()
        continue
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break

    while True:
      try:
        self._math = int(input("수학 점수 입력 => "))
        if self._math < 0 or self._math > 100:
          raise BetweenNumException()
      except ValueError as e:
        print("숫자를 입력해 주세요(%s)\n" % e)
        print()
        continue
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break


  def process_sungjuk(self ):

    self._tot = self._kor + self._eng + self._math
    self._avg = self._tot / 3


    if self._avg >= 90:
      self._grade = "수"
    elif self._avg >= 80:
      self._grade = "우"
    elif self._avg >= 70:
      self._grade = "미"
    elif self._avg >= 60:
      self._grade = "양"
    else:
      self._grade = "가"

  def output_sungjuk(self):
    print("%4s %3s %4d  %4d  %4d  %4d  %5.2f  %2s" %
          (self._hakbun, self._irum, self._kor, self._eng, self._math,
           self._tot, self._avg, self._grade))

if __name__ == "__main__":
  obj = Sungjuk()
  obj.input_sungjuk()
  obj.process_sungjuk()
  obj.output_sungjuk()
