strQuestion = '''
    1. 0~9 까지 출력
    2. 1 ~ 10 까지 출력
    3. 1 ~ 100 까지 출력
    4. 1 ~ 100 까지 3의 배수 출력
    5. 1 ~ 10 까지의 합 출력
    6. 1 ~ 100 까지 홀수의 합 출력
    7. 두 수를 입력하여 작은 수에서 큰 수 까지 출력
    예)     3 7 : 3 4 5 6 7
            9 6 : 6 7 8 9
    8. 반복문을 중첩하여 구구단을 출력하시오.

'''

print(strQuestion)
# 1.
print("1번----------")
for letter in range(0,10):
    print(letter)
# 2.
print("2번----------")
for letter in range(1,11):
    print(letter)
# 3.
print("3번----------")
for letter in range(1,101):
    print(letter)
# 4.
print("4번----------")
for letter in range(1,101):
    if letter % 3 == 0:
        print(letter)
# 5.
print("5번----------")
sum =0
for letter in range(1,11):
     sum += letter
print(sum)

# 6.
print("6번----------")
sum =0
for letter in range(1,101):
    if letter % 2 == 1:
        print(letter)
        sum += letter
print(sum)

# 7.
print("7번----------")
i = 0
num1 = int(input("두 수를 입력하세요 : "))
num2 = int(input("두 수를 입력하세요 : "))
if num1 > num2:
    print(num1, num2, ": ", end = " ")
    for letter in range(num2,num1+1):
        print(letter, end = " ")
else:
    print(num1, num2, ": ", end = " ")
    for letter in range(num1,num2+1):
        print(letter, end = " ")

# 8.
# 구구단 세로
for vertical in range(1,10):
    for horizon in range(2,10):
        print(horizon, " * ", vertical, "= ", horizon * vertical, end = "\t")
        if horizon == 9:
            print()
print()

# 구구단 가로
for vertical in range(2,10):
    for horizon in range(1,10):
        print(vertical, " * ", horizon, "= ", vertical * horizon)



strQuestion = '''
    1 ~ 100 사이에 3, 6, 9 가 있는 수 리스트 만들기
'''
tempList = list()
for letter in range(1,101):
    if "3" in str(letter) or "6" in str(letter) or "9" in str(letter):
        tempList.append((str(letter)))
print(tempList)
