# datetime 모듈을 사용
import datetime
today = datetime.datetime.now()
print(today)
print(type(today))
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.hour)
# print(today.minute)
# print(today.second)
print(str(today.year) +'년 '+str(today.month)+'월 '+str(today.day)+'일')
print(f'{today.year}년 {today.month}월 {today.day}일')
