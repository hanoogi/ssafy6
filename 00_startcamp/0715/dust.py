import requests


# key = 'AIiP14yZQkZ7gURpstTASJFBtokqG8l3u5lJDAmhTS6s6XnhlEzO3Q34J%2FCX0Zu5fVsAtL1nKrSFqlA0067OuQ%3D%3D'
# url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=json'
# 
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=AIiP14yZQkZ7gURpstTASJFBtokqG8l3u5lJDAmhTS6s6XnhlEzO3Q34J%2FCX0Zu5fVsAtL1nKrSFqlA0067OuQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EA%B2%BD%EB%B6%81&ver=1.0'
response = requests.get(url).json()

print(response)
print(type(response))


"""
실습
'sidoName의 미세먼지 농도는 pm10value입니다.'라는 메시지를 출력하시오.
"""
sido_name = response['response']['body']['items'][0]['sidoName']
dust = response['response']['body']['items'][0]['pm10Value']

print(f'{sido_name}의 미세먼지 농도는 {dust}입니다.')

