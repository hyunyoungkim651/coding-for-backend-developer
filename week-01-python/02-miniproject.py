# 방금 배운 클래스 복습
# 학교 클래스를 만들어라
# 학교 클래스는 이름, 설립연도, 주소라는 정보를 가지고 있어야 한다.
# 클래스를 활성화 할 때, 위의 3가지 데이터를 반드시 입력하도록 처리해라

class School:
    def __init__(self, snamne, syear, saddress):
        self.sname = snamne
        self.syear = syear
        self.saddress = saddress

school_inf = School("온천초등학교", 1899, "부산시 동래구 우장춘로")
print("학교 이름 : {}, 설립 연도 : {}, 주소 : {}".
format(school_inf.sname, school_inf.syear, school_inf.saddress))
