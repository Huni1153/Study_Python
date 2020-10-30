strQuestion = '''
# 문1) 다음 코드를 for문을 사용하여 구현하시오
#     입력값을 3 -> [[3, 4, 5], [6, 7, 8]]
# a=[] #이속에 리스트 2개를 만들어야 한다.( +=, extend, append 셋 중 하나)
# #[[],[]] #비어있는 리스트안에 비어있는 리스트 2개 넣기
# #[[1,2,3],[4,5,6]] #리스트안에 첫번째 리스트에 1,2,3 넣기


####################
반복문을 사용하여 사용자 입력을 리스트에 추가하시오
####################
 정수를 입력 [1/5]: 1
[1]
 정수를 입력 [2/5]: 2
[1, 2]
 정수를 입력 [3/5]: 3
[1, 2, 3]
 정수를 입력 [4/5]: 0


###################
Str + replace
다음 문자열을 수정 하시오
###################
password is 1234
수정 후 : password is 5678

매일 많은 환자가 발생합니다.
수정 후 : 항상 많은 코로나 환자가 발생합니다.


###################
Split + 반복문 사용
###################
url = 'http://www.naver.com/news/today=20200131'
user = 'name:홍길동 age:22 sex:남자 nation:대한민국'

위 문자열을 보고 다음과 같이 출력하시오

['http:', 'www.naver.com', 'news', 'today=20200131']
name -> 홍길동
age -> 22
sex -> 남자
nation -> 대한민국



####################
반복문을 사용하여 '지구'를 'earth'로 바꾸시오
####################


space= ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성','지구']


['태양', '수성', '금성', 'earth', '화성', '목성', '토성', '천왕성', '해왕성', 'earth']


####################
다음 디셔너리의 값을 모두 합하고 평균을 구하시오
####################
covid = {'January':4500, 'February':5000, 'March':2500, 'April':1200,
'May':567, 'June':434, 'July':323}

dict_values([4500, 5000, 2500, 1200, 567, 434, 323])
환자수 총계: 14524
환자수 평균: ???





####################
1~100사이의 랜덤값 하나를 만들어 맞추는 프로그램(10문 10답처럼)
####################

가령 랜덤 값하나가 64 이였다.

숫자 맞추기 게임 (1~100사이 값중 하나를 고르시오)
숫자 입력 : 50

50보다는 큰 숫자 입니다.
숫자 입력 : 75

75보다는 작은 숫자 입니다.
숫자 입력 : 65

65보다는 작은 숫자 입니다.
숫자 입력 : 64

정답입니다. 4번 만에 숫자를 맞춤

####################
1~100까지 3진수를 출력하시오.
####################
'''

# 1.

listTemp = list()
intInput = 0
idx = 0

while True:

    intInput = input("정수 입력[" + str(idx) + "/5] : ")

    if not intInput.isnumeric():
        print("정수를 입력하세요!")
        continue

    intInput = int(intInput)
    listTemp.append(intInput)
    print(listTemp)
    idx += 1

    if idx == 5:
        break

# 2.

strReplace = "password is 1234"
print(strReplace.replace('1234','5678'))

strReplace = "매일 많은 환자가 발생합니다."
print(strReplace.replace("매일","항상"))

# 3.

urlStr = "http://www.naver.com/news/today=202000131"
userStr = "name:홍길동 age:22 sex:남자 nation:대한민국"

strUrl = urlStr.split("/")
strUrl.remove("")
strUser = userStr.split(" ")

print(strUrl)
for vertical in range(0,len(strUser)):
    print(strUser[vertical])

# 4.

# for문
space = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']

for vertical in range(0,len(space)):
    if space[vertical] in '지구':
        space[vertical] = 'earth'
print(space)

# while문
space = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
num = 0
cnt = space.count('지구')
while True:
    if space[num] == '지구':
        space[num] = 'earth'
        cnt -= 1
    num += 1
    if cnt == 0:
        break
print(space)


# 5.
covid = {'January' : 4500, 'February' : 5000, 'March' : 2500, 'April' : 1200, 'May' : 567, 'June' : 434, 'July' : 323}
print(covid.values())
dSum = 0

listValue = list(covid.values())
for dIndex in range(len(listValue)):
    dSum += listValue[dIndex]
print(dSum)
print(dSum // dIndex)


# 6.

import random

randomValue = random.randrange(1,101)
inputValue = 0
cnt = 0
print("숫자 맞추기 게임 (1 ~ 100)사이 값중 하나를 입력하시오.")
while True:
    inputValue = int(input("숫자 입력 : "))
    if inputValue < 0 or 100 < inputValue:
        print("1 ~ 100사이의 값만 입력하세요!")
        continue
    else:
        cnt += 1
        if randomValue == inputValue:
            print("정답입니다! 정답은 : " + str(inputValue) + " / " + str(cnt) + "번 만에 숫자를 맞춤")
            break
        elif randomValue > inputValue:
            print(str(inputValue) + "보다는 큰 숫자 입니다.")
        elif randomValue < inputValue:
            print(str(inputValue) + "보다는 작은 숫자 입니다.")



