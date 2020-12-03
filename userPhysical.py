import main

def recordTime(toDate):
    f=open('phyRecordData.txt','a', encoding='UTF8')
    f.write(toDate)
    f.close

def comPhy(date):
    f=open('phyRecordData.txt','r', encoding='UTF8')
    phy = f.readlines()
    for line in phy:
        item = line.split(" ")
        toDay = item[item.index(date)]
    f.close

def BmiCal(Height, Weight):
    bmi = Weight * (Height * Height)
    print("BMI 지수 : " + bmi)

