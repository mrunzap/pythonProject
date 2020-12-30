import time
import random
import pygame
import sqlite3
import datetime

conn = sqlite3.connect('./resource/record.db',isolation_level=None)
cursor =  conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,cor_cnt INTEGER, record text,regi_date text)")


# 영어 단어 리스트
words = []     # resource 폴더에서 word.txt 불러와서 words 변수에 담는다.
n = 1          # 게임시도 횟수
cor_cnt = 0    # 정답 횟수
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
# 불러온 파일 리스트에 담기
with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())  # 양쪽 공백 제
# 사용자의 입력값을 받았을 때 시작함(동기:Sync)

input( 'ready Press Enter Key!')

# time 게임 시작 시간을 담기위 한 time패키지 사용
startTime = time.time()

# words 변수에 담긴 1000개의 단어sadf를 존나 섞어야 된다.답
while n <=5:
    random.shuffle(words)
    pickUpSentense = random.choice(words)
    print()
    print('Question # {}'.format(n))
    print()
    print(pickUpSentense)
    userInput = input()

    # 문자가 들어오지만 안전하게 형변환을 한다.그리고 공백제거 실시
    if str(userInput).strip() == str(pickUpSentense).strip():
        print("정답")
        pygame.mixer.music.load("./sound/good.wav")
        pygame.mixer.music.play()
        # 정답일 때 정답변수 1씩 증가
        cor_cnt += 1
    else:
        print("오답")
        pygame.mixer.music.load("./sound/bad.wav")
        pygame.mixer.music.play()
    n += 1
# 게임 끝
# 게임 결과 보여주기
endTime = time.time()
durationTime = endTime - startTime
durationTime = format(durationTime,'.3f')
if cor_cnt > 3 :
    print("합격")
else:
    print('불합격')
# 수행시간 출력
print('게임시간 : ',durationTime,'정답횟수:{}'.format(cor_cnt))

cursor.execute("INSERT INTO RECORDS('COR_CNT','RECORD','REGI_DATE') VALUES (?,?,?)",
               (cor_cnt,durationTime,datetime.datetime.now().strftime('%Y-%M-%D %H %M %S')))

# 시작 지점
if __name__ == '__main__':
    pass

# DB생성 & AutoCommit
# 본인 DB 경로