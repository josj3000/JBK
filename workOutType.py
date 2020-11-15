while True:
    workOutType = input("운동 부위를 선택해주세요.\n1. 가슴 운동\n2. 등 운동\n3. 하체 운동\n4. 어깨 운동\n5. 팔 운동\n")
    if workOutType == "1":
        chestType = input("가슴 운동을 선택해주세요.\n1. 벤치 프레스\n2. 인클라인\n3. 디클라인\n4. 플라이\n")
        chestSet = input("세트수와 횟수를 입력해주세요.")
    elif workOutType == "2":
        backType = input("등 운동을 선택해주세요.\n1. 렛풀다운\n2. 로우\n3. 풀업\n")
        backSet = input("세트수와 횟수를 입력해주세요.")
    elif workOutType == "3":
        legType = input("하체 운동을 선택해주세요.\n1. 스쿼트\n2. 파워 레그 프레스\n3. 데드리프트\n4. 레그 컬\n")
        legSet = input("세트수와 횟수를 입력해주세요.")
    elif workOutType == "4":
        shoulderType = input("어깨 운동을 선택해주세요.\n1. 숄더 프레스\n2. 밀리터리 프레스\n3. 레터럴 레이즈\n")
        shoulderSet = input("세트수와 횟수를 입력해주세요.")
    elif workOutType == "5":
        armType = input("팔 운동을 선택해주세요.\n1. 이두 컬\n2. 삼두근(다운)\n")
        armSet = input("세트수와 횟수를 입력해주세요.")

