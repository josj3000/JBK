print('사용자 정보를 입력해주세요.')
userName = input('이름 : ')
userAge = input('나이 : ')
userGender = input('성별(남성, 여성) : ')
while userGender!="남성"or"여성":
    print("신체 정보 계산을 위해 입력 양식을 준수해주세요.")
    userGender = input('성별(남성, 여성) : ')
    
userHeight = input('키 : ')
userWeight = input('몸무게 : ')


print('1. 운동 이력 갱신')
print('2. 신체 변화 관리')
Chose = input('기능을 선택해주세요.\n')

if Chose=="1":

    WorkOutType=input('.')

while Chose=="2":
    WorkOut=input('.')
    