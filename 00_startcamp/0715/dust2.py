import requests

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?'
apikey = 'pxMYp9JSAcMSOWwfcT71Z8sOqMrNPrQqbdZwIbx03u8bzY65gKa8oDNXF1ACao8V6NJAFFPFTdFK3ojdHq%2BR4A%3D%3D'
returnType = 'json'
numOfRows = '10'
pageNo = '1'
sidoName = "경북"
ver = "1.0"
# sidoName,pm10Value

# 1. 발급 받은 api key로 미세먼지 정보 요청 보내기
data = requests.get(url=url+'serviceKey='+apikey +'&sidoName='+sidoName +'&ver='+ver + '&numOfRows=' + numOfRows + '&pageNo=' + pageNo + '&returnType=' + returnType).json()

from pprint import pprint
pprint(data)
# print(data)

sidoName = data['response']['body']['items'][0]['sidoName']
# 2. 응답 받은 데이터로 sidoNmae, pm10Value 출력하기
print(sidoName)
print(data['response']['body']['items'][0]['pm10Value'])