import requests

name = 'kim'
url = f'https://api.nationalize.io?name={name}'
response = requests.get(url).json()

print(response)
print(type(response))

"""
실습
ㅇㅇ의 국적은 ㅇㅇ%로 ㅇㅇ입니다. 라고 출력 해보세요. 
(여러 국가 출력시 가장 높은 것만)
"""
name = response['name']
country_id = response['country'][0]['country_id']
country_probability = int(response['country'][0]['probability'] * 100)

print(f'{name}의 국적은 {country_probability}%로 {country_id}입니다.')