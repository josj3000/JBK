from datetime import datetime
import timedelta
import userPhysical
import workOutType


print('오늘의 날짜를 다음과 같이 입력해주세요.\n예시) 2020-01-01')
ToDay = input('날짜 : ')
print('사용자 정보를 입력해주세요.')
userName = input('이름 : ')
userAge = input('나이 : ')

userGender = input('성별을 선택해주세요\n1. 남성\n2. 여성\n')
while True:
    if userGender not in '1':
        if userGender not in '2':
            print("올바른 입력을 해주세요.")
            userGender = input('성별을 선택해주세요\n1. 남성\n2. 여성\n')
            continue
    break

userHeight = int(input('키 : '))
userWeight = int(input('몸무게 : '))


print('1. 운동 이력 갱신')
print('2. 신체 변화 관리')
Chose = input('기능을 선택해주세요.\n')

while True:
    if Chose not in '1':
        if Chose not in '2':
            print("올바른 입력을 해주세요.")
            print('1. 운동 이력 갱신')
            print('2. 신체 변화 관리')
            Chose = input('기능을 선택해주세요.\n')
            continue
    break

if Chose == '1':
    now = datetime.ToDay()
    nowDate = now.strftime('%Y-%m-%d')
    workOutType.write_txt(nowDate)
    workOutType.Chose

if Chose == '2':
    userPhysical.recordTime(ToDay)