
# csv 파일 바로 불러오기
import csv

f = open("output.csv", "w", encoding="utf-8", newline='')
# newline='' : 줄이 두 번씩 띄어지는 문제 방지 (CSV 작성 시 필수)


# quotechar = "'" : 데이터를 묶을 문자 지정
# csv.QUOTE_ALL : 모두 사용하겠단 의미
# delimiter : 구분자, 기본적으로 , 를 사용함
wr = csv.writer(f, delimiter=',', quotechar="'",quoting=csv.QUOTE_ALL)
print(wr)
wr.writerow((1, "김미정", False)) # 행 단위로 추가한다
wr.writerow([2, "박상미", True])

f.close()

#############################################################################
import csv

fp = open("output.csv", "r", encoding="utf-8", newline='')
reader = list(csv.reader(fp)) # 2차원 구조로 출력
print(reader)
for row in reader: # 한 행식 읽어서 출력
    print(row)

fp.close()