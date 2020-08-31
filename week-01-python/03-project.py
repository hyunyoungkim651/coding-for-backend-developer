# 구현 내용
#
# 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
# 힌트
#
# 리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
# 앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
# 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.
import random

win = 0
lose = 0

ROCK = "바위"
SCISSORS = "가위"
PAPER = "보"
RSP_LIST = (
    ROCK,
    SCISSORS,
    PAPER
)


while win < 3 and lose < 3:
    # 유저 선택
    user = input("{}, {}, {}: ".format(SCISSORS, ROCK, PAPER))
    # 컴퓨터 임의 선택
    ai = random.choice(RSP_LIST)

    if user == ai:
        print("비겼습니다.")
    elif user not in RSP_LIST:
        print("가위, 바위, 보 중에서 하나를 선택해주세요.")
    elif ((user == ROCK and ai == "SCISSORS") or
        (user == SCISSORS and ai == PAPER) or
        (user == PAPER and ai == ROCK)):
        print("이겼습니다.")
        win += 1
    else:
        print("졌습니다.")
        lose += 1

if(win == 3):
    print("사용자가 이겼습니다.")
    print("최종 스코어 win : {}, lose : {}".format(win, lose))
else:
    print("컴퓨터가 이겼습니다.")
    print("최종 스코어 win : {}, lose : {}".format(win, lose))
    


    # if user == "SCISSORS":
    #     if ai == "ROCK":
    #         print("컴퓨터 승..")
    #         lose += 1
    #     elif ai == "PAPER":
    #         print("사용자 승!!")
    #         win += 1
    #     else:
    #         print("비겼습니다.")
    #
    # if user == "바위":
    #     if ai == "보":
    #         print("컴퓨터 승..")
    #         lose += 1
    #     elif ai == "가위":
    #         print("사용자 승!!")
    #         win += 1
    #     else:
    #         print("비겼습니다.")
    #
    # if user == "보":
    #     if ai == "가위":
    #         print("컴퓨터 승..")
    #         lose +=1
    #     elif ai == "바위":
    #         print("사용자 승!!")
    #         win +=1
    #     else:
    #         print("비겼습니다.")
    #
    # if win == 3:
    #     print("사용자가 이겼습니다.")
    #     print("최종 스코어 win : {}, lose : {}".format(win, lose))
    #     break;
    #
    # if lose == 3:
    #     print("컴퓨터가 이겼습니다.")
    #     print("최종 스코어 win : {}, lose : {}".format(win, lose))
    #     break;
