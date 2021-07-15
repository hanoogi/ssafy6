import requests

name = 'lee'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()
# print(response)
# print(type(response))

# 'o o 의 나이는 o o 입니다.
name = response['name']
age = response['age']
print(f"{response['name']}의 나이는 {age} 입니다.")
