class NoInput(Exception):
  def __init__(self):
    super().__init__("아무것도 입력하지 않았습니다.")

class NegativeNumException(Exception):
  def __init__(self):
    super().__init__("양수를 입력해 주세요")

class SameKeyException(Exception):
  def __init__(self):
    super().__init__("동일한 상품이 있습니다. 다시 입력해 주새요.")



class Sangpum:
  def __init__(self):
    self._code = ""
    self._irum = ""
    self._su = 0
    self._price = 0
    self._kumack = 0
    self._tot = 0

  def get_code(self):
    return self._code
  def set_code(self, code):
    self._code = code
  code = property(get_code, set_code)

  def get_irum(self):
    return self._irum
  def set_irum(self, irum):
    self._irum = irum
  irum = property(get_irum, set_irum)

  def get_su(self):
    return self._su
  def set_su(self, su):
    self._su = su
  su = property(get_su, set_su)

  def get_price(self):
    return self._price
  def set_price(self, price):
    self._price = price
  price = property(get_price, set_price)

  def get_kumack(self):
    return self._kumack
  def set_kumack(self, kumack):
    self._kumack = kumack
  kumack = property(get_kumack, set_kumack)

  def get_tot(self):
    return self._tot
  def set_tot(self, tot):
    self._tot = tot
  tot = property(get_tot, set_tot)

  def input_sangpum(self, lst):  ## 동일한 이름을 넣을 경우
    while True:
      try:
        self._code  = input("제품코드 입력 => ")
        for obj in lst:
          if self._code  == obj.code:
            raise SameKeyException()
          elif self._code .strip() == "":
            raise NoInput()
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break

    self.update_sangpum()

  def update_sangpum(self):
    while True:
      try:
        self._irum = input("이름 입력 => ")
        if self._irum.strip() == "":
          raise NoInput()
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break

    while True:
      try:
        self._su = int(input("수량 입력 => "))
        if self._su < 0:
          raise NegativeNumException()
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
        self._price = int(input("단가 입력 = => "))
        if self._price < 0:
          raise NegativeNumException()
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


  def process_sangpum(self ):

    self._kumack = self._su * self._price


  def output_sangpum(self):
    print("%4s     %4s    %4d    %4d    %6d" %
          (self._code , self._irum, self._su, self._price, self._kumack))

if __name__ == "__main__":
  obj = Sangpum()
  obj.input_sangpum()
  obj.process_sangpum()
  obj.output_sangpum()
