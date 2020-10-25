# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

words = []       # 영어 단어 리스트(1000개 로드)

n = 1           # 게임 시도 횟수
cor_cont = 0    # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words) # 단어 리스트 확인

input("Ready? Press Enter Key!") # Enter Game Start!

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)    # 문제 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip(): # 입력 확인(공백 제거)
        print("Pass!")
        cor_cont += 1
    else:
        print("Wrong!")

    n +=1 # 다음 문제 전환

end = time.time()       # End Time
et = end - start        # 총 게임시간
et = format(et, ".3f")  # 소수 셋째 자리 출력(시간)

if cor_cont >= 3:
    print("합격")
else:
    print("불합격")

# 수행 시간 출력
print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cont))

# 시작 지점
if __name__ == '__main__':
    pass



