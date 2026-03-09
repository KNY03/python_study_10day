from 곽나영_0309_02 import Sangpum, NoInput

lst = []

## 만약 리스트에 똑같은 같이 이미 있으면 다시 인풋을 받아라

def menu_title():
  print("*** 상품관리 ***")
  print("1. 상품정보 입력")
  print("2. 상품정보 출력")
  print("3. 상품정보 조회")
  print("4. 상품정보 수정")
  print("5. 상품정보 삭제")
  print("6. 프로그램 종료")
  print()


def input_sangpum():
  print()
  obj = Sangpum()
  obj.input_sangpum(lst)
  obj.process_sangpum()
  #global lst
  lst.append(obj)
  print("\n상품 입력 성공!!!\n")

def print_sangpum():
  if len(lst) == 0:
    print("\n출력할 데이터가 없음!!\n")
    return
  else:
    print("")
    print("\n\t\t\t *** 제품관리 ***")
    print("=============================================")
    print("제품코드   제품명     수량      단가    판매금액")
    print("=============================================")
    total = 0
    for obj in lst:
      obj.output_sangpum()
      total += obj.kumack
    print("===============================================")
    print("\t\t\t\t\t\t 총금액 : %7d" % total)

def search_sangpum():
  if len(lst) == 0:
    print("\n조회할 데이터가 없음!!\n")
    return

  while True:
    code = input("\n조회할 상품번호 입력 => ")
    for obj in lst:
      if obj.code == code:
        print("제품코드   제품명     수량      단가    판매금액")
        print("=============================================")
        obj.output_sangpum()
        print("=============================================")
        break
    else:
      try:
        print("\n조회할 상품 정보가 없음2!!\n")
        if code.strip() == "":
          raise NoInput()
      except Exception as e:
        print("예외가 발생하였습니다(%s)\n" % e)
        print()
        continue
      else:
        break
    break


def update_sangpum():
  if len(lst) == 0:
    print("\n수정할 데이터가 없음1!!\n") # 레이즈 사용
    return

  code = input("\n수정할 상품번호 입력 => ")
  for obj in lst:
    if obj.code == code:
      print()
      obj.update_sangpum()
      obj.process_sangpum()
      print("\n상품 %s 정보 수정 성공!!\n" % code)
      break
  else:
    print("\n수정할 상품 정보가 없음2!!!\n")# 레이즈 사용

def delete_sangpum():
  if len(lst) == 0:
    print("\n삭제할 데이터가 없음1!!\n")
    return

  code = input("\n삭제할 상품코드 입력 => ")
  for obj in lst:
    if obj.code == code:
      lst.remove(obj)
      print("\n상품 %s 정보 삭제 성공!!\n" % code)
      break
  else:
    print("\n삭제할 상품 정보가 없음2!!!\n") # 레이즈 사용

if __name__ == "__main__":
  while True:
    menu_title()
    try:
        menu = int(input("메뉴를 선택하세요(1~6) => "))
    except ValueError as e:
        print("숫자로 입력해 주세요(%s)\n" % e)
        print()
        continue

    if menu == 1:
      input_sangpum()
    elif menu == 2:
      print_sangpum()
    elif menu == 3:
      search_sangpum()
    elif menu == 4:
      update_sangpum()
    elif menu == 5:
      delete_sangpum()
    elif menu == 6:
      print("\n프로그램 종료!!")
      break
    else:
      print("\n메뉴를 다시 입력하세요!!\n")
