# 숫자
number = 3
print(type(number))
number2 = 1.5
print(type(number2))
# 문자열
string = '문자열'
print(type(string))
# boolean(논리값)
boolean = True
print(type(boolean))

# 형변환
string_number = '3'
print(int(string_number) + 3)
print(string_number + str(3))

# f-string
name = '홍길동'
print(f'내 이름은 {name}입니다.')

# 리스트 
my_list =['java', 'django']
print(my_list[1])
my_list[0] = 'python'
print(my_list[0])
print(len(my_list))

# 딕셔너리 
my_home = { 
    'location': 'gumi', 
    'area-code': '054',
}

print(my_home['location'])
# print(my_home['name'])
print(my_home.get('location'))
print(my_home.get('name'))

my_home['location'] = 'seoul'
print(my_home['location'])