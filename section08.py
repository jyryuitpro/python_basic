# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print(Fibonacci.fib2(400))
print(Fibonacci().title)

# 사용2(클래스)
from pkg.fibonacci import *

print(Fibonacci.fib2(600))
print(Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

print(fb.fib2(1600))
print(fb().title)

# 사용4(함수)
import pkg.calculations as c
print(c.add(10, 100))
print(c.mul(10, 100))

# 사용5(함수)
from pkg.calculations import div as d
print(int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))