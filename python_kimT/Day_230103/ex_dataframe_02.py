#-----------------------------------------------------------------------------
# 데이터 프레임(Data Frame) 요소 다루기
# ------------------------------------------------------------------------------------
# 패키지, 모듈 로딩 ================================= #pdf 파일 38페이지 ~ 참고하기
import pandas as pd

# DF 생성 실습 =--------------------------------------
# 데이터 => List 데이터 사용
data = [[10, 20, 30], ['F','M', 'M'], [11,22,33], [44,55,66], ['A', 'B', 'C']] #===> 2차원

df1 = pd.DataFrame(data)

#DF 요소/원소 다루기 ---------------------------------------------------
# 열(coulumn) 기준으로 요소 
# 0번 컬럼 가져오기 => 변수명[컬럼]
print(f'columns => {df1.columns}')
one = df1[0]  # => 0번 컬럼의 10과 F가 출력
print(f'one => {type(one)}\n{one}')

#모든 컬럼을 다 가져오고 싶을 경우, 반복문을 돌리면 된다. 
print('----------------------------------------')
for col in df1.columns:
    print(f'one => {type(df1[col])}\n{df1[col]}')


# 여러개 컬럼(열) 요소 가져오기 => 변수명[컬럼1, 컬럼2]
# 0번, 2번 컬럼 가져오기
oneTwo = df1[[0,2]]
print(f'oneTwo => {type(oneTwo)}\n{oneTwo}')


# 범위 지정 후 요소 가져오기 => 변수명[시작:끝+1]
# 0번, 1번 컬럼 가져오기
### 슬라이싱은 범위지정하여 컬럼 데이터 추출 안됨!!!
oneZero = df1[0:1] #슬라이싱 이용 #컬럼의 슬라이싱으로는 행으로 나오지 않음
print(f'oneZero => {type(oneZero)}\n{oneZero}')




#DF 요소/원소 다루기 열(column) ------------------------------------------------
# 데이터 프레임의 컬럼 속성 변경하기 ===> 변수명.속성명 = 새로운 값
df1.columns = ['One', 'Two', 'Three'] #=> 속성을 str 으로 변경 시 object로 변경됨
print(f'변경 확인: {df1.columns}')



# 'One' 컬럼 가져오기 => 변수명[컬럼], 변수명.컬럼명
# 단, 컬럼이 문자열 str 인 경우
# 단, 1개 컬럼만 가능
print(f'[{df1["One"]}] => {type(df1["One"])}\n{df1["One"]}')
print(f'[df1.One] => {type(df1.One)}\n{df1.One}')

# 시리즈 인덱스는 행 인덱스이다.
# 컬럼 지정시 자동으로 가져오는 0,1,2... 는 못가져옴
# 즉, 컬럼 인덱스 변경 후 기본 인덱스 사용 불가
#print(f'[df1.[0]] => {type(df1[0])}\n{df1[0]}') #=> 오류가 발생함, key error




#DF 요소/원소 다루기 행(row) ------------------------------------------------
#변수명.iloc[인덱스] : 반드시 정수형 인덱스만 가능
#변수명.loc[인덱스]  : 문자열 인덱스 가능

# 0번 행 데이터 가져오기 

print(f'==================row \n{df1}')
zeroRow=df1.iloc[0]
print(f'zeroRow => {type(zeroRow)}\n{zeroRow}')


# 2개 행 데이터 가져오기 => 변수명.iloc[[인덱스, 인덱스]]
zeroTwoRow = df1.iloc[[0,1]]
print(f'zeroTwoRow => {type(zeroTwoRow)}\n{zeroTwoRow}')
# => 데이터 프레임이 된다.


# 범위 지정 후 지정 데이터 가져오기 ==> 변수명.iloc[시작:끝+1]
#                                    변수명.iloc[시작:끝+1] (출력값이 같다)  
# 슬라이싱할 때 row 를 가져온다.
oneThree = df1.iloc[1:4]
print(f'oneThree => {type(oneThree)}\n{oneThree}')

oneThee2=df1[1:4]
print(f'oneThee2 => {type(oneThee2)}\n{oneThee2}')


# 행(row) 인덱스 속성 변경 후 행 추출 ------------------------------------------
df1.index=['A', 'B', 'C', 'D', 'E']
print(f'행 인덱스 속성 변경 확인 => {df1.index}')

zeroRow=df1.loc['A'] # 문자열이니까 loc
#zeroRow=df1.loc[0] # 오류가 뜬다.
zeroRow=df1.iloc[0] # iloc 'i' 가 붙어있으면 정수를 써야한다.



# 요소/원소 (Elemnet) 추출하기 -----------------------------------------------------------
print('--------------------<요소 원소 추출하기>----------------------------------------')
print(df1)
print('------------------------------------------------------')

# 사용법 : 변수명.iloc[행인덱스, 열인덱스], 변수명.iloc[행인덱스, 열인덱스]
# 사용법 : 변수명.loc[행인덱스, 열인덱스], 변수명.loc[행인덱스, 열인덱스]
# 요소값이 33인 데이터, 22인 데이터 추출

v33 = df1.loc['C', 'Three']
v22 = df1.loc['C']['Two']
print(f'v33 => {v33}, v22 => {v22}')

# 요소값이 44인 데이터, 66인 데이터 추출

v44 = df1.loc['D', 'One']
v66 = df1.loc['D']['Three']
print(f'v44 => {v44}, v66 => {v66}')

v4466 = df1.loc['D', ['One', 'Three']]
print(f'v4466 => \n{4466}')

# 요소값이 20, 30, 22, 33인 데이터 추출

values = df1.loc[['A', 'C']] [['Two', 'Three']]
print(f'values => \n{values}')

values1 = df1.iloc[[0,2], [1,2]]
print(f'values => \n{values1}')


# 삭제하기
#기본값은 행 axis = 0, 열 axis = 1