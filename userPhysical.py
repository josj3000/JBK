

def recordTime(toDate, Hei, Wei):
    f=open('phyRecordData.txt','a', encoding='UTF8')
    m=open('count.txt','r+', encoding='UTF8')
    cot = int(m.readline())+1
    f.write(toDate+'\n')
    f.write('키 : ' + Hei + '\n체중 : ' + Wei)
    f.write('\n------'+str(cot)+'\n')
    m.seek(0)
    m.write(str(cot))
    m.truncate()
    f.close
    m.close

def comPhy(date, nowD):
    f=open('phyRecordData.txt','r', encoding='UTF8')
    m=open('count.txt','r', encoding='UTF8')
    lines = f.readlines()
    mLine = m.readline()
    i=0
    for a in mLine:
        if lines[i] == date+'\n':
            print(lines[i+1])
            print(lines[i+2])
            print("▽▽▽▽▽\n"+lines[-3]+lines[-2])           
            break
        else :
            count = 0
            count = count + 1
            if count == lines[-1]:
                print('해당 날짜에 기록이 없습니다.')
        i=i+1
    f.close

def BmiCal(Height, Weight):
    
    bmi = Weight // ((Height/100) * (Height/100))
    print("BMI 지수 : " + str(bmi))

