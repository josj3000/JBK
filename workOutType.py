def write_txt(txt):
    f=open('workOutData.txt','a', encoding='UTF8')
    f.write(txt)
    f.close

def Chose():
    while True:
        workOutType = input("운동 부위를 선택해주세요.\n1. 가슴 운동\n2. 등 운동\n3. 하체 운동\n4. 어깨 운동\n5. 팔 운동\n")
        if workOutType == "1":
            chestType = input("가슴 운동을 선택해주세요.\n1. 벤치 프레스\n2. 인클라인\n3. 디클라인\n4. 플라이\n")
            if chestType == "1":    chestType = "벤치 프레스"
            elif chestType == "2":    chestType = "인클라인"
            elif chestType == "3":    chestType = "디클라인"
            elif chestType == "4":    chestType = "플라이"
            chestSet = input("세트수와 횟수를 입력해주세요.")
            choice= input(("계속 하시겠습니까?\n1. 네\n2. 아니오"))
            if choice=="1":
                write_txt(" " + chestType + "\n")
                write_txt(" " + chestSet + "\n")
                continue
            elif choice=="2":  
                write_txt(" " + chestType + "\n")         
                write_txt(" " + chestSet  + "\n" + "------")         
                break
        elif workOutType == "2":
            backType = input("등 운동을 선택해주세요.\n1. 렛풀다운\n2. 로우\n3. 풀업\n")
            if backType == "1":    backType = "렛풀다운"
            elif backType == "2":    backType = "로우"
            elif backType == "3":    backType = "풀업"
            backSet = input("세트수와 횟수를 입력해주세요.")
            choice= input(("계속 하시겠습니까?\n1. 네\n2. 아니오"))
            if choice=="1":
                write_txt(" " + backType + "\n")
                write_txt(" " + backSet + "\n")
                continue
            elif choice=="2":  
                write_txt(" " + backType + "\n")         
                write_txt(" " + backSet  + "\n")         
                break
        elif workOutType == "3":
            legType = input("하체 운동을 선택해주세요.\n1. 스쿼트\n2. 파워 레그 프레스\n3. 데드리프트\n4. 레그 컬\n")
            if legType == "1":    legType = "스쿼트"
            elif legType == "2":    legType = "파워 레그 프레스"
            elif legType == "3":    legType = "데드리프트"
            elif legType == "4":    legType = "레그 컬"
            legSet = input("세트수와 횟수를 입력해주세요.")
            choice= input(("계속 하시겠습니까?\n1. 네\n2. 아니오"))
            if choice=="1":
                write_txt(" " + legType + "\n")
                write_txt(" " + legSet + "\n")
                continue
            elif choice=="2":  
                write_txt(" " + legType + "\n")         
                write_txt(" " + legSet  + "\n")         
                break
        elif workOutType == "4":
            shoulderType = input("어깨 운동을 선택해주세요.\n1. 숄더 프레스\n2. 밀리터리 프레스\n3. 레터럴 레이즈\n")
            if shoulderType == "1":    shoulderType = "숄더 프레스"
            elif shoulderType == "2":    shoulderType = "밀리터리 프레스"
            elif shoulderType == "3":    shoulderType = "레터럴 레이즈"
            shoulderSet = input("세트수와 횟수를 입력해주세요.")
            choice= input(("계속 하시겠습니까?\n1. 네\n2. 아니오"))
            if choice=="1":
                write_txt(" " + shoulderType + "\n")
                write_txt(" " + shoulderSet + "\n")
                continue
            elif choice=="2":  
                write_txt(" " + shoulderType + "\n")         
                write_txt(" " + shoulderSet  + "\n")         
                break
        elif workOutType == "5":
            armType = input("팔 운동을 선택해주세요.\n1. 이두 컬\n2. 삼두근(다운)\n")
            if armType == "1":    armType = "이두 컬"
            elif armType == "2":    armType = "삼두근(다운)"
            armSet = input("세트수와 횟수를 입력해주세요.")
            choice= input(("계속 하시겠습니까?\n1. 네\n2. 아니오"))
            if choice=="1":
                write_txt(" " + armType + "\n")
                write_txt(" " + armSet + "\n")
                continue
            elif choice=="2":  
                write_txt(" " + armType + "\n")         
                write_txt(" " + armSet  + "\n")         
                break