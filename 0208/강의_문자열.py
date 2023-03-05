'''
1. 컴퓨터에서의 문자표현
-글자 A를 메모리에 저장하는 방법에 대해서 생각해보자
-물론 칼로 A라는 글자를 새기는 방식은 아닐 것이다. 메모리는 숫자만을 저장할 수
있기 때문에 A라는 글자의 모양 그대로 비트맵으로 저장하는 방법을 사용하지 않는 한
(이 방법법은 메모리 낭비가 심하다) 각 문자에 대해서 대응되는 숫자를 정해 놓고
이것을 메모리에 저장하는 방법이 사용될 거이다.
-영어가 대소문자 합쳐서 52이므로 6(64가지)비트면 모두 표현할 수 있다.
이를 코드체계라고 한다.
000000 -> 'a', 000001 -> 'b'
-그런데 네트위크가 발전되기 전 미국의 각 지역 별로 코드체계를 정해놓고 사용했지만
-네트워크가 발전하면서 서로간에 정보를 주고 받을 때 정보를 달리 해석하면서
문제가 생겼다.
-그래서 혼동을 피하기 위해 표준안을 만들기로 했다.
-바로 이러한 목적으로 1967년, 미국에 ASCII라는 문자 인코딩 표준이 제정되었다.
'''

'''
2. 유니코드 인코딩 (UTF : Unicode Transformation Format)

3. 문자열(string)
3.1 fixed length
3.2 variable length
3.2.1 length controlled
3.2.2 delimited

4. Python 에서의 문자열 처리
-문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는
인덱싱, 슬라이싱 연산들을 사용할 수 있음
-문자열 클래스에서 제공되는 메소드
replace(),split(),isalpha(),find()
-문자열은 튜플과 같이 요소값을 변경할 수 없음(immutable)

5. 문자열 뒤집기
-자기 문자열에서 뒤집는 방법이 있고 새로운 빈 문자열을 만들어
소스의 뒤에서부터 읽어서 타겟이 쓰는 방법이 있다.
-자기 문자열을 이용할 경우는 swap을 위한 임시 변수가 필요하며
반복 수행을 문자열 길이의 반만을 수행해야 한다.
ex)문자열 길이가 9 일때는 4번 반복

6.PYthon에서 문자열 뒤집기
s = [::-1]
or
s = list(s)
s.reverse()
s = ''.join(s)
'''


def strlen(a):
    i = 0
    while a[i] != '\0':
        i += 1
    return i


a = ['a', 'b', 'c', '\0']
print(strlen(a))


s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'
print(s1 == s2)  # True
print(s1 is s2)  # True
print(s1 == s5)  # True
print(s1 is s5)  # False

# 문자받아와서 숫자로 반환하기


def atoi(data):
    result = 0
    for i in range(len(data)):
        # 49 - 48 = 1
        result = result * 10 + ord(data[i]) - ord('0')

    return result


result = atoi('45421')
print(result, type(result))
# 숫자를 문자열로 만들기


def itoa(data):
    result = ''
    while data > 0:
        remain = data % 10
        result = chr(remain + ord('0')) + result
        data = data // 10
    return result


result = itoa(45421)
print(result, type(result))
