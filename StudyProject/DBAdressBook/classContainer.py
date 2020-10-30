from noDBAdressBook import classContent

class Container():
    # 생성자
    def __init__(self):
        self.listContent = list()
        print("Container 생성자 호출")

    # def setListContent(self, listContent): # set메소드
    #     self.listContent = listContent
    #
    # def getListContent(self): # get메소드
    #     return self.listContent

    def addContent(self, inputName, inputAge, inputTel):
        dataContent = classContent.Content(inputName, inputAge, inputTel)
        self.listContent.append(dataContent)

    def modifyContent(self,selectNum, inputName, inputAge, inputTel):
        selectNum -= 1
        data = self.listContent[selectNum]
        data.setName(inputName)
        data.setAge(inputAge)
        data.setTel(inputTel)

    def viewContent(self):
        if(len(self.listContent)) == 0:
            print("입력된 데이터가 없습니다.")
            return 0

        for viewCnt in range(len(self.listContent)):
            print(str(viewCnt + 1) + ".\t\t", end = "")
            data = self.listContent[viewCnt]
            print(data.getName() + "\t\t" + str(data.getAge()) + "\t\t" + data.getTel())
            cntReturn = viewCnt + 1

        return cntReturn

    def deleteContent(self,selectNum):
        selectNum -= 1
        del self.listContent[selectNum]
