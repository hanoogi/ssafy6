# 경로 문제때문에 실행 안됨. 한글 폴더 없애야
import requests

name = 'kim'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()

print(response)


"""
실습
"""
# name = response['name']
# age = response['age']
# print(f'{name}의 나이는 {age}입니다.')

