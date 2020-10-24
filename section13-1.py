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

print(words) # 단어 리스트 확인

input("Ready? Press Enter Key!") # Enter Game Start!

start = time.time()

