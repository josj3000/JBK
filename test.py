from datetime import datetime
import timedelta

now = datetime.today()
nowDate = now.strftime('%Y-%m-%d')

print(nowDate)


"""
now = datetime.today()
nowDate = now.strftime('%Y-%m-%d')

test1 = input()
f = open("data.txt", 'a')
f.write(test1 + ' ')
f.close

test2 = input()
f = open("data.txt", 'a')
f.write(test2)
f.close
"""