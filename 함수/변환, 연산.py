# 변환

a = int(input())
print('%x' %a)    # 10진수 -> 16진수_소문자
print('%X' %a)    # 10진수 -> 16진수_대문자

b = input()
n = int(b,16)     # 입력된 b를 16진수로 변환
print('%o' %n)    # 16진수 -> 8진수

# ord()는 문자를 유니코드 값으로 변환
c = ord(input())  # 문자 -> 10진수 변환 
print(c)

#chr()는 정수를 유니코드 문자로 변환
d = int(input())
print(chr(c))     # 정수 -> 유니코드문자 변환

# 연산

# shift 연산
print(n<<1)       # n을 2배 한 값이 출력된다.
print(n>>1)       # n을 반으로 나눈 값이 출력된다.
print(n<<2)       # n을 4배 한 값이 출력된다.
print(n>>2)       # n을 반으로 나눈 후 다시 반으로 나눈 값이 출력된다.
print(a<<b)       # a를 2^b 만큼 곱한 값이 출력된다.

# 거듭제곱
a**b              # a^b의 값을 구한다.

