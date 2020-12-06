f=open('phyRecordData.txt','a', encoding='UTF8')
m=open('count.txt','r+', encoding='UTF8')
cot = int(m.readline())+1
f.write('2020-12-06\n')
f.write('키 : 170\n체중 : 70')
f.write('\n------'+str(cot)+'\n')
m.seek(0)
m.write(str(cot))
m.truncate()
f.close
m.close