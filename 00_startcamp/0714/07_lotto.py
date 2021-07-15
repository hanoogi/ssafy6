# 1. random 친구를 불러 온다.
import random
# 2. 1부터 45 까지의 숫자를 저장한다.
numbers = range(1, 46)
# 3. random 모듈의 sample 함수를 통해 6개의 숫자를 무작위로 뽑아 
#    새로운 박스에 저장한다.
lotto = random.sample(numbers, 6)
# 4. 새로운 박스를 출력한다.
print(lotto)
