# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
    print("Yes")

# 예2
if False:
    print("No")

# 예3
if False:
    print("No")
else:
    print("Yes2")

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1, True
# 거짓 : "", [], (), {}, 0, False

city = ""
# city = "1"

if city:
    print(">>>>True")
else:
    print(">>>>False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print(a > b and b > c)
print(a > b or c > b)
print(not a > b)
print(not False)
print(not True)



