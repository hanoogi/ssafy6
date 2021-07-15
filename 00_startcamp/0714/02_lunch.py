# menu라는 리스트를 만들어 보자
# 그 안에 저녁 메뉴를 3가지 넣어보자
# 큰따옴표, 작은 따옴표 모두 가능

# 1. 함수가 포함된 코드를 불러온다.
import random
# 2. 점심메뉴 리스트를 만든다.
menu = ['짬뽕','육전', '마라탕']
# 3. 함수를 통해 얻은 결과 값을 저장한다. 
choice = random.choice(menu)
# 4. 출력해본다.
print(choice)
# print(menu)
# print(menu[1])