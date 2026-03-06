from 곽나영_0305_02 import Sungjuk

# import sys, os
#
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sample_problems"))
#
# from sungjuk_05_class import Sungjuk # 빨간 줄은 뜨지만 사용이 가능함

lst = []

def menu_title():
    print("\n*** 성적관리 ***")
    print("1. 성적정보 입력: ")
    print("2. 성적정보 출력: ")
    print("3. 성적정보 조회: ")
    print("4. 성적정보 수정: ")
    print("5. 성적정보 삭제: ")
    print("6. 프로그램 종료: ")
    print()

def input_sungjuk():
    sungjuk = Sungjuk()
    sungjuk.input_info()
    sungjuk.input_score()
    sungjuk.calc_grade()
    lst.append(sungjuk)
    print("\n추가되었음\n")

def print_sungjuk():
    if len(lst) == 0:
        print("\n데이터가 없음!!\n")
        return
    else:
        print("")
        print("\t\t\t   ***성적표***\t\t\t\t\t\t")
        print("=================================================")
        print("  학번  이름  국어  영어  수학  총점  평균  등급")
        print("=================================================")
        tot_avg = 0
        for i in lst:
            i.output_grade()
            tot_avg += i.avg
        print("==================================================")
        print("\t\t\t\t\t 총 학생수: %d\t\t 평균 성적: %.2f" % (len(lst), tot_avg/len(lst))) # 학생수는 len(rd)로도 할 수 있음

def search_sungjuk():
    if len(lst) == 0:
        print("\n데이터가 없음!!\n")
        return
    else:
        data_num = (input("찾고싶은 학생번호를 입력하시오: "))
        found = False

        for i in lst:
            if data_num == i.num:
                print("")
                print("\t\t\t   ***성적표***\t\t\t\t\t\t")
                print("=================================================")
                print("  학번  이름  국어  영어  수학  총점  평균  등급")
                print("=================================================")
                i.output_grade()
                print("==================================================")
                found = True
                break
        if not found:
            print("\n해당 학생은 없습니다.\n")

def update_sungjuk():
    if len(lst) == 0:
        print("\n데이터가 없음!!\n")
        return
    else:
        data_num = (input("수정하고 싶은 학생번호를 입력하시오: "))
        found = False

        for i in lst:
            if data_num == i.num:
                print("")

                i.name = (input("이름을 다시 작성해 주세요: "))
                i.kor = int(input("국어 성적을 다시 작성해 주세요: "))
                i.eng = int(input("영어 성적을 다시 작성해 주세요: "))
                i.math = int(input("수학 성적을 다시 작성해 주세요: "))

                i.calc_grade()
                found = True
                break
        if not found:
            print("\n해당 학생은 없습니다.\n")

def delete_sungjuk():
    if len(lst) == 0:
        print("\n데이터가 없음!!\n")
        return
    else:
        data_num = (input("삭제하고 싶은 학생번호를 입력하시오: "))
        found = False

        for i in lst:
            if data_num == i.num:
                print("")
                lst.remove(i)
                found = True
                break
        if not found:
            print("\n해당 학생은 없습니다.\n")

if __name__ == '__main__':
    while True:
        menu_title()
        menu = int(input("\n메뉴를 선택하시오(1~6): "))
        print()
        if menu == 1:
            input_sungjuk()
        elif menu == 2:
            print_sungjuk()
        elif menu == 3:
            search_sungjuk()
        elif menu == 4:
            update_sungjuk()
        elif menu == 5:
            delete_sungjuk()
        elif menu == 6:
            print("\n프로그램을 종료합니다!")
            break
        else:
            print("\n메뉴를 다시 입력하시오!\n")