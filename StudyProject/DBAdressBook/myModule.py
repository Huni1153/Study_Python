from noDBAdressBook import classContainer

def myAdress():

    containerData = classContainer.Container() # container 객체 생성

    while True:
        display()
        inputNum = input("번호를 입력하세요(1 ~ 5번) : ")

        if not inputNum.isnumeric(): # 문자 예외처리
            print("!!!!!!!!!!숫자만 입력하라고?")
            continue

        inputNum = int(inputNum) # 입력받은 값을 정수로 캐스팅 여기서 캐스팅한 이유는 문자 예외처리가 된 후 정수를 비교연산 하기 위해서

        if inputNum <= 0 or 5 < inputNum:
            print("!!!!!!!!!!1 ~ 5번만 누르라고?")
            continue

        print()
        if inputNum == 1:
            add(containerData)

        elif inputNum == 2:
            modify(containerData)

        elif inputNum == 3:
            view(containerData)

        elif inputNum == 4:
            delete(containerData)

        elif inputNum == 5:
            break

def display():
    for displayWord in ("========== 전화번호부 ==========\n", "1. 추가", "2. 수정", "3. 조회", "4. 삭제", "5. 종료"):
        print(displayWord)

def add(containerData):
    # print("추가")
    inputName = input("이름을 입력하세요 : ")
    inputAge = checkAge() # 양의 정수를 입력받기 위해 checkAge()함수 호출
    inputTel = input("전화번호를 입력하세요 : ")
    containerData.addContent(inputName, inputAge, inputTel) # containerData의 addContent()함수 호출

def modify(containerData):
    # print("수정")
    checkNum = containerData.viewContent()

    if checkNum != 0:
        selectNum = checkPositiveInt(checkNum,"수정")
        inputName = input("이름을 입력하세요 : ")
        inputAge = checkAge() # 양의 정수를 입력받기 위해 checkAge()함수 호출
        inputTel = input("전화번호를 입력하세요 : ")
        containerData.modifyContent(selectNum, inputName, inputAge, inputTel) # containerData의 modifyContent()함수 호출

    else:
        return

def view(containerData):
    # print("조회")
    print("번호\t\t이름\t\t\t나이\t\t번호")
    if containerData.viewContent() > 0:
        input("다음으로 넘어가려면 아무키나 누르세요.")
    
def delete(containerData):
    # print("삭제")
    checkNum = containerData.viewContent() # 사용자가 쉽게 삭제하기 위해 조회기능을호출하여 리스트의 index값을 리턴받는다.

    if checkNum != 0: # 리턴받은 index값이 0이 아니라면
        selectNum = checkPositiveInt(checkNum,"삭제") # 양의 정수를 입력받는 함수 호출
        containerData.deleteContent(selectNum) # 이렇게 입력받은 index번호를 container에 정의된 삭제 함수에 전달인자를 보내 호출

    else:
        return

def checkAge(): # 입력받은 값이 음수이지 않고 150 이상이 아닌 양의 정수를 받게하여 리턴하는 함수.
    while True:
        inputAge = input("나이를 입력하세요 : ")

        if not inputAge.isnumeric():  # 입력받은 값이 문자일때 예외처리
            print("나이만 입력하라구요?")
            continue

        inputAge = int(inputAge)  # 입력받은 나이를 정수로 캐스팅

        if inputAge < 0:  # 나이가 음수일리 없고
            print("나이가 음수일리가 없잖아?")
            continue

        elif inputAge > 150:  # 150살 이상일리도 없고
            print("에이 말도안돼?")

        else:
            return inputAge

def checkPositiveInt(checkNum, strStyle): # 입력받은 값이 문자와 음수가아닌 양의정수를 받게하여 리턴하는 함수
    while True:
        selectNum = input("무엇을 "+ strStyle +" 하시겠습니까?(1 ~ " + str(checkNum) + ") : ")

        if not selectNum.isnumeric(): # 문자예외 처리
            print("1 ~ " + str(checkNum) + "사이의 값만 입력하세요.")
            continue

        selectNum = int(selectNum)

        if selectNum > checkNum or selectNum < 0: # 양수값만 허용
            print("1 ~ " + str(checkNum) + "사이의 값만 입력하세요.")
            continue

        else:
            return selectNum
