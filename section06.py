# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#     code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
def send_sms(world):
    print("Hello ", world)

send_sms("Python!")
send_sms(7777)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제4(데이터 타입 반환)
def func_mul2(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1, y2, y3]
    # return (y1, y2, y3)

lt = func_mul2(100)
print(lt)