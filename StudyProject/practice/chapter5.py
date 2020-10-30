# 문자열 타입으로 변환 : str()함수를 사용하면 다른 데이터 타입을 문자열로 변환할 수 있다.
# ex)
print(str(98.6)) # 결과 : 98.6
print(str(1.0e4)) # 결과 : 10000.0
print(str(True)) # 결과 : True
# 위 결과값은 모두 문자열이다.
# 문자열이 아닌 객체를 print()로 호출하거나 문자열 포매팅(string formatting)을 사용할 때, 파이썬은 내부적으로 str()함수를 사용한다.

# 이스케이프 문자 : \(백슬래시)
# \n : 줄바꿈, \t : 탭 \" : 큰 따옴표, \' : 작은 따옴표 \\ : 백슬래시

# 결합하기 : + 연산자로 문자열과 문자열을 결합할 수 있다. ex) "안녕" + "하세요" = "안녕하세요"
# 문자열을 결합할 때 공백을 자동으로 붙이지 않는다. print()함수는 각 인수 사이에 공백을 붙이고 마지막에는 줄바꿈을 붙인다.
a = "안녕"
b = "하십"
c = "니까"
# a+b+c결과 : 안녕하십니까
# print(a,b,c)결과 : 안녕 하십 니까

# 복제하기 : * 연산자로 문자열을 복제할 수 있다.
# ex)
print("Ha!" * 3) # 결과 : Ha!Ha!Ha!

# 문자 추출 : [] 문자열에서 하나의 문자를 추출하기 위해서 문자열 이름 뒤에 대괄호([])와 오프셋을 지정한다.
# 가장 왼쪽의 오프셋은 0이고 그다음은 1,2,... 가장 오른쪽의 오프셋은 -1이고 그다음은 -2,-3,...이런 식으로 진행된다.
# ex)
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[0]) # 결과 : a
print(letters[-1]) # 결과 : z

# 슬라이스로 부분 문자열 추출 : 슬라이스를 사용하여 한 문자열에서 문자열 일부를 추출할 수 있다. 제일 마지막
# 정의 방법은 대괄호안에 옵션으로 스탭(step)을 명시하여 슬라이스를 정의한다.
# [:] : 처음부터 끝까지 전체 시퀀스를 추출한다.
# [start:] : start 오프셋부터 끝까지 시퀀스를 추출한다.
# [:end] : 처음부터 (end -1) 오프셋까지 시퀀스를 추출한다.
# [start : end] : start 오프셋부터(end -1)오프셋까지 시퀀스를 추출한다.
# [start : end : step] : step만큼 문자를 건너뛰면서, start오프셋부터 (end -1)오프셋까지 시퀀스를 추출한다.
# 파이썬은 마지막 오프셋은 포함하지 않는다. !!!!이거였다.
# ex)
letters = "abcdefghijklmnopqrstuvwxyz" # 0 ~ 25 , -1 ~ -26
print(letters[:]) # 결과 : abcdefghijklmnopqrstuvwxyz 전체 문자열을 추출한다.
print(letters[20:]) # 결과 : uvwxyz 오프셋 20부터 문자열 끝까지 추출한다.
print(letters[10:]) # 결과 : klmnopqrstuvwxwz 오프셋 10부터 문자열 끝까지 추출한다.
print(letters[12:15]) # 결과 : mno 오프셋 12부터 14까지 추출한다.
print(letters[-3:]) # 결과 : xyz 오프셋 -3부터 끝까지 추출한다.
print(letters[18:-3]) # 결과 : stuvw 오프셋 18부터 -3까지 추출한다.
print(letters[-6:-2]) # 결과 : uvwx 오프셋 -6부터 -2까지 추출한다.
print(letters[::7]) # 결과 : ahov 1보다 큰 스텝을 원한다면 3번째 콜론뒤에 숫자를 명시한다.처음부터 7스텝씩 건너뛰면서 추출한다.
print(letters[4:20:3]) # 결과 : ehknqt 오프셋 4부터 20까지 3스텝씩 건너뛰면서 추출한다.
print(letters[19::4]) # 결과 : tx 오프셋 19부터 끝까지 4스텝씩 건너뛰면서 추출한다.
print(letters[:21:5]) # 결과 : afkpu 처음부터 오프셋 21까지 5스텝씩 건너뛰면서 추출한다.
print(letters[-1::-1]) # 결과 : zyxwvutsrqponmlkjihgfedcba 오프셋 -1부터 끝까지 -1스텝씩 건너뛰면서 추출한다.
print(letters[-1::1]) # 결과 : z 오프셋 -1부터 시작하지만 1스텝씩 건너뛰면서 추출하니 z만 출력된다.
print(letters[::-1]) # 결과 : zyxwvutsrqponmlkjihgfedcba 오프셋을 생략했지만 -1스텝씩 건너뛰면서 추출하기 때문에 z부터 a까지 추출한다.
print(letters[-50:]) # 결과 : abcdefghijklmnopqrstuvwxyz 오프셋 -50부터 끝까지 추출한다. -24부터 a이고 그 전부터 추출해도 a부터 추출된다어
print(letters[-51:-50]) # 결과 : 오프셋 -51부터 -50까지 추출하지만 추출되는건 없다.
print(letters[:70]) # 결과 : abcdefghijklmnopqrstuvwxyz 처음 부터 오프셋 7까지 추출한다.
print(letters[70:71]) # 결과 : 오프셋 70부터 71까지 추출하지만 추출되는건 없다. 24:25도 마찬가지

# 문자열 길이 : len()함수는 문자열의 길이를 센다.
# ex)
empty = ""
print(len(letters)) # 결과 : 26
print(len(empty)) # 결과 : 

# 문자열 나누기 : split() 어떤 구분자를 기준으로 하나의 문자열을 작은 문자열들의 리스트로 나눈다.
# ex)
tasks = '너무,졸리다,집에 가고싶다'
print(tasks)
print(tasks.split(',')) # 결과 : ['너무', '졸리다', '집에 가고싶다']
# 구분자를 지정하지 않으면 문자열안에 줄바꿈, 스페이스, 탭을 사용하여 구분한다.
print(tasks.split())
tasks = tasks.split(',')
print(tasks[1])

