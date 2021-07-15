# 1. 주어진 정수 n의 절대값을 구하시오.
n = 10
if n < 0:
    n = n * -1
print(n)

# 2. 주어진 양수 n이 홀수, 짝수인지 판별하여 출력하는 코드를 작성하시오.
n = 10
if n % 2 == 0:
    print('짝수')
else:
    print('홀수')

# 3. 주어진 정수 n이 양수, 음수, 0인지 판별하시오.
n = 10
if n > 0:
    print("양수")
elif n < 0:
    print("음수")
#elif n == 0:
else:
    print("0")

numbers = [1, 2, 3]    
for number in numbers:  # 1, 2, 3
    print(number)

for i in range(len(numbers)): # 0, 1, 2
    print(numbers[i])

# 합구하기
sum = 0
for number in numbers:  # 1, 2, 3
    sum = sum + number  # 0+1, 1+2, 3+3
print(sum)

sum = 0
for i in range(len(numbers)):  # 1, 2, 3
    sum = sum + numbers[i]  # 0+1, 1+2, 3+3
print(sum)

# 리스트 숫자들의 홀수를 판별
for number in numbers:  # 1, 2, 3
    if number % 2 == 1:   
        print(number) 
