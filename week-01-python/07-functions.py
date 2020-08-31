# 함수 functions

def hello_friends(name):
    print("hi, {}".format(name))


name1 = "marco"
name2 = "jane"
name3 = "jone"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "jone"
name8 = "tom"

# print("hi, {}".format(name_1))
# print("hi, {}".format(name_2))
# print("hi, {}".format(name_3))
# print("hi, {}".format(name_4))
# print("hi, {}".format(name_5))
# print("hi, {}".format(name_6))
# print("hi, {}".format(name_7))
# print("hi, {}".format(name_8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 1) 입력값 o, 반환값 o
def sum(a, b):
    return a + b
# 2) 입력값 o, 반환값 x
def hello_friend(name):
    print("hello, {}".format(name))

# 3) 입력값 x, 반환값 o
def return_1():
    return 1
# 4) 입력값 x, 반환값 x
def hello_world():
    print("hello world")

num_1 = return_1()
print(num_1)

# 입력값 parameters, 반환값 return
