# 구현 내용
#
# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
# 힌트
#
# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.
import random

korea = ["비빔밥", "불고기", "된장 찌개", "김치 찌개"]
china = ["짜장면", "군만두", "탕수육", "짬뽕"]
japan = ["스시", "우동", "모밀", "돈가스"]
select = input("한식, 중식, 일식 중 한 가지를 고르시오. : ")

if select == "한식":
    # select_choice = random.choice(korea)
    select_result = korea[random.randint(0, len(korea))]
elif select == "중식":
    select_result = random.choice(china)
elif select == "일식":
    select_result = random.choice(japan)
else:
    print("한식, 중식, 일식 중에서 선택하셔야 됩니다.")

if select_result:
    print("{} 중에서 {}가 선택 되었습니다.".format(select, select_result))
