# 자료형 : int, float, str, bool

int_var = 1
print(int_var)
print(type(int_var))

float_var = 3.14
print(float_var)
print(type(float_var))

bool_var = True
print(bool_var)
print(type(bool_var))

bool_var = False
print(not bool_var)
print(type(bool_var))

str_var = "hello python!"
print(str_var)
print(type(str_var))

#문자열 인덱싱
print(str_var[0])
print(str_var[1])
print(str_var[2])
print(str_var[3])
print(str_var[4])

# 문자열 슬라이싱
print(str_var[6:])
print(str_var[6:12])
print(str_var[6:-1])

# 컬렉션 자료형
list_var = [1, 3.14, "hello", True]
print(list_var[2])
print(list_var[0:2])
print(list_var[:2])
list_var[0] = 1.5               # mutable 변경 ㄱㄴ
print(list_var)

tuple_bar = 1, 2, 3
print(tuple_bar)
print(tuple_bar[0:2])
print(tuple_bar[:2])
# tuple_bar[0] = 1.5            # immutable 변경 불ㄱㄴ

# set_bar = set()
set_bar = {1,2,3}
print(set_bar)
print (type(set_bar))

set_bar.add(1)
set_bar.add(1)
set_bar.add(1)     # 중복 허용하지 않음
print(set_bar)

set_bar.add(2)
set_bar.add(3)
set_bar.add(4)
print(set_bar)
print(list("apple"))
print(set("apple"))              # 순서 보장하지 않음

dict_var = {}
print(type(dict_var))
dict_var["사과"] = 5
dict_var["포도"] = 3
dict_var["포도"] = 2
print(dict_var)
print(dict_var["사과"])
print(dict_var.get("딸기"))
print(dict_var.get("딸기", 0))