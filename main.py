from datetime import datetime
import timedelta
import userPhysical
import workOutType


print('사용자 정보를 입력해주세요.')

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
    now = datetime.today()
    nowDate = now.strftime('%Y-%m-%d')
    workOutType.write_txt(nowDate)
    workOutType.Chose()

if Chose == '2':
    now = datetime.today()
    nowDate = now.strftime('%Y-%m-%d')
    userPhysical.recordTime(nowDate, str(userHeight), str(userWeight))
    print("1. BMI 계산\n2. 신체 변화 확인")
    TwoChose = input('기능을 선택해주세요.')
    if TwoChose == '1':
        userPhysical.BmiCal(userHeight, userWeight)
    elif TwoChose == '2':
        print('어느 날짜부터의 변화를 확인할지 선택해주세요.')
        search = input('예시) 2020-01-01\n')
        userPhysical.comPhy(search, nowDate)


