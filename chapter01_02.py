# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student Class
    Author : jy.ryu.itpro
    Date : 2020.10.30
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1

# Self 의미
student1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 55})
student2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'stu2@naver.com')

print(id(student1))
print(id(student2))

# ID 확인
a = 'ABC'
b = a

print(student1._name == student2._name)
print(student1 is student2)
print(a == b) # 값 비교
print(a is b) # id 비교

# dir & __dict__ 확인

print(dir(student1))
print(dir(student2))

print()
print()

print(student1.__dict__)
print(student2.__dict__)

# Doctring
print(Student.__doc__)
print()

# 실행
student1.detail_info()
student2.detail_info()

# 에러
# Student.detail_info()

Student.detail_info(student1)
Student.detail_info(student2)

# 비교
print(student1.__class__, student2.__class__)
print(id(student1.__class__) == id(student2.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장x)

# student1._name = 'HAHAHA'

print(student1._name, student2._name)
print(student1._email, student2._email)

print()
print()

# 클래스 변수

# 접근
print(student1.student_count)
print(student2.student_count)
print(Student.student_count)

print()
print()

# 공유 확인
print(Student.__dict__)
print()
print(student1.__dict__)
print()
print(student2.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del student2

print(student1.student_count)
print(Student.student_count)







