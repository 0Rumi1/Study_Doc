#--------------------------------------------------------------------------------------
# 데코레이터(Decorator) : 메서드에 명확한 의미 부여
# 형식 : @XXXX
#--------------------------------------------------------------------------------------
# 클래스 및 메서드 종류
# - 완성된 클래스 => 클래스
# - 미완성 클래스 => 추상클래스(Abstract Class)
#                   미구현(코드 없는 메서드) 메서드를 가지고 있는 클래스
#                   abc모듈 포함해서 사용함
#--------------------------------------------------------------------------------------
# 메서드 종류
# - 객체 생성 해야만 사용가능한 메서드 => self
#   - 인스턴스 메서드
# - 객체 생성 없이 사용가능한 메서드 => cls
#   - 정 적  메서드 --> 객체 없이 사용 가능
#   - 클래스 메서드 --> 클래스 정보를 가지고 객체 없이 사용 가능
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# 학생 정보 클래스
# - 클래스명 : Student
# - 속    성 : 
#           - 클 래 스 속성 : school
#           - 인스턴스 속성 : name, number, grade
# - 메서드
#       - 클래스 메서드 : 학교명 출력 기능
#       - 정  적 메서드 : 학교명 출력 기능
#--------------------------------------------------------------------------------------
# - 오버로딩(Overloading)
#   - 같은 이름의 다른 매개변수 종류, 갯수
#   - 상속과 관계없이 사용 가능
# - 오버라이딩(Overiding)
#   - 상속 관계에서 사용 가능
#   - 부모의 메서드
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
# 정보 은닉(캡슐화)
# __속성명 : 비공개 즉, 객체 변수로 쓸 수 없음
# 읽기 : get속성명
# 쓰기 : set속성명
#__a메서드명()
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------


class Student:
    #클래스 속성
    school='대구 중학교'

    # 인스턴스 즉 객세 생성 및 초기화 메서드
    def __init__(self, name, number, grade):
        self.name=name
        self.number=number
        self.gradd=grade


    #객체 미생성으로 사용 가능한 메서드들
    @staticmethod
    def showSchoolName(count):
        Student.school = 'Happy 중학교'
        print(f'[classmethod ]School => {Student.school} - {count}')

    @classmethod #클래스 정보를 넘겨주는 것 
    def printSchool(cls, count):
        print(f'cls ===> {cls}')
        print(f'[classmethod ]School => {cls.school} - {count}')



#--------------------------------------------------------------------------------------
# 대학생 정보를 담고 있는 클래스
# 클래스명 : BigStudent
# 속    성 : 학교, 이름, 번호, 학년, 전공
#--------------------------------------------------------------------------------------

class BigStudent(Student):
    # 클래스 변수
    school='한국대학교'


    # 인스턴스 즉 객체 생성 및 속성 초기화 메서드
    def __init__(self, name, number, grade, major):
        super().__init__(name, number, grade)
        self.major=major



#클래스 및 객체 사용-----------------------------------------------------------------------
print(Student.school)
Student.showSchoolName(1)
Student.printSchool(1)

BigStudent.showSchoolName(2) #정적 메서드
BigStudent.printSchool(2)    #클래스 메서드

#클래스 안에 들어 있으면 함수 아니고 메서드, 클래스에 속해 있지 않으면 함수 