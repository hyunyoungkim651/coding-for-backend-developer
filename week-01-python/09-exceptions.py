# exceptions 예외(버그)

# ZeroDivisionError
# 1 / 0

# 예외 처리
# try except 문


# def divide_by(first, second):
#     try:
#         return first / second
#     # except :
#     except ZeroDivisionError:
#         return "0으로 나눌 수 없습니다."
#
# # 4 / 2 = 2
# print(divide_by(4, 2))
# print(divide_by(4, 0))


# 예외 만들기
# Exception

# class 이름은 앞에 대문자로하기로 약속
class EvenNumberDivisionError(Exception):
    pass # 지금 당장 구현하지 않고 넘어 가겠다.

# 함수의 이름은 소문자로
def divide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDivisionError # 에러를 일으킨다.

    else:
        return first / second

print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))
