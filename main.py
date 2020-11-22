from datetime import datetime
import timedelta
import test
import Physical
import workOutType

print('사용자 정보를 입력해주세요.')
userName = input('이름 : ')
userAge = input('나이 : ')

userGender = input('성별을 선택해주세요\n1. 남성\n2. 여성\n')
if userGender != '1' or '2' :
    print("올바른 입력을 해주세요.")
    while True:
        userGender = input('성별을 선택해주세요\n1. 남성\n2. 여성\n')
        if userGender == '1':
            break
        elif userGender == '2':
            break
    
userHeight = int(input('키 : '))
userWeight = int(input('몸무게 : '))


print('1. 운동 이력 갱신')
print('2. 신체 변화 관리')
Chose = input('기능을 선택해주세요.\n')

if Chose == "1":
    now = datetime.today()
    nowDate = now.strftime('%Y-%m-%d')
    workOutType.write_txt(nowDate)
    workOutType.Chose

elif Chose == "2":
    Physical