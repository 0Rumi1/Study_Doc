#----------------------------------------------------------------------------------------------
# 모듈 및 패키지 살펴보기
# [조건] 동일한 목표/목적로 구성됨
# - 모  듈 : 변수, 함수, 클래스를 하나의 파일로 묶은 것
# - 패키지 : 모듈들을 하나로 묶은 것
#----------------------------------------------------------------------------------------------
# [사용법]
# 모듈안의 모든 것 포함하기
# import 모듈명                         => 모듈명.변수명, 모듈명.함수, 모듈명.클래스
# import 모듈명 as 별칭                 => 별칭.변수명, 별칭.함수, 별칭.클래스
# 모듈안에서 선택한 것만 포함하기-----------------------------------------------------------------
# from 모듈명 import 변수, 함수, 클래스  => 변수명, 함수, 클래스 (일부만 가져옴)
#-----------------------------------------------------------------------------------------------



# 파이썬 기본 제공 모듈, 표준모듈
import math as m        # 모듈 전체 포함
from math import pow    # 모듈에서 선택한 것만 포함
from math import *      # * 아스타리크 의미 : 모든 것 => 모듈명을 작성하지 않아도 된다는 차이점이 있음, 함수명() 만 작성하면 됨 

# 포함한 모듈 사용하기 
print(m.pi)              #모듈명.변수명
print(m.factorial(5))    #모듈명.함수명()
print(pow(2,3))          #함수명() => 모듈명 지정하지 않아도 됨   
print(factorial(4))

# 임의의 수 생성 관련 모듈 사용  =================================================================
import random as r

#임의의 숫자를 1개 출력
#random() : a.a <~<=1.0 사이의 임의의 실수 반환 (범위 지정 X)
for _ in range(10):
    print(round(r.random()*10,2), end='') #round 소숫점 2자리 이하 버리고 출력

print('\n -----------------------')
#범위지정 임의의 정수 숫자 1개 출력
#randint(sNum, eNum) : sNum <= ~ <= eNum : 

for _ in range(10):
    print(r.randint(1,5), end= ' ')
print('\n -----------------------')


# 지정된 범위에서 임의의 숫자 범위 생성
#randrage(start, end, step)
r.randrange(10)
print(r.randrange(1, 10, 2))

# MyLotto --------------------------------------------------------------------------------------
# 숫자 1~ 45
# 중복 불허
# 임의의 6개 숫자
# 리스트와 셋을 각각 사용시 조건문을 사용하느냐의 차이다.

import random as r
for _ in range(6):
    while True:
        pass
print(r.randrange(1,46), end = ' ') #중복 체크 오류 있음 => 수정 필요
    # 대부분 데이터는 중복 체크가 필수



choiceNum = []
while True:
    if len(choiceNum) == 6: break
    num = r.randint(1, 45) # => 무조건 1씩 증가함, 따라서 사용이 제한적일 수 있음
    if num not in choiceNum:
        choiceNum.append(num)
        
    
    #중복 체크 오류 있음 => 수정 필요
    # 대부분 데이터는 중복 체크가 필수


# 파일 입출력 open() 함수랑 함께 사용 -----------------------------------------------------------

import os.path

FILE_NAME = 'Good.txt'
if not os.path.exists(FILE_NAME): #파일이 존재하는지 확인하는 모듈, 존재하지 않으면 if 문 True 값 출력
    print("존재하는 파일인지 체크하세요!")
fp = open(FILE_NAME, mode = 'r', encoding= 'utf=8')
print(fp.read())
fp.close



import pandas as pd
choiceNum = []
    if len(choiceNum) == 30: break
    num = r.randint(1, 45) # => 무조건 1씩 증가함, 따라서 사용이 제한적일 수 있음
    if num not in choiceNum:
        choiceNum.append(num)