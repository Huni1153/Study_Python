import sys
import ctypes

from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QRegExpValidator


class Content(QWidget):
    def __init__(self):
        super().__init__()

        self.mydll = ctypes.windll.LoadLibrary('C:\Huni_Project\Pycharm_Project\pyqt5_Project\Dll2.dll')
        self.mydll.datainit.restype = ctypes.c_int  # c라이브러리의 datainit()함수의 리턴타입 지정
        self.rand = self.mydll.datainit()

        self.mydll.playball.argtype = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.mydll.playball.restype = ctypes.POINTER(ctypes.c_int * 2)

        self.mydll.hint.argtype = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.mydll.hint.restype = ctypes.POINTER(ctypes.c_int * 999)

        self.setupUI()

    def setupUI(self):

        # self.setGeometry(800, 200, 500, 300)

        # leftGroupBox이름의 GroupBox 생성
        self.leftGroupBox = QGroupBox("입력")

        # leftInnerLayOut이름의 BoxLayout 생성
        self.leftInnerLayOut = QGridLayout()

        # leftInnerLayOut에 추가할 화면 생성 여기에다!!!!
        regExp = QRegExp("[0-9]{0,3}")
        self.inputNumber = QLineEdit(self)
        self.inputNumber.setValidator(QRegExpValidator(regExp, self))
        self.submitBtn = QPushButton("확인")
        self.resStrike = QLabel(self)
        self.resBall = QLabel(self)
        self.probabilityRes = QLabel(self)
        self.hintBtn = QPushButton("힌트 받기")
        self.resetBtn = QPushButton("리셋")

        self.leftInnerLayOut.addWidget(self.inputNumber, 0, 0)
        self.leftInnerLayOut.addWidget(self.submitBtn, 0, 1)
        self.leftInnerLayOut.addWidget(QLabel("Strike : "), 1, 0)
        self.leftInnerLayOut.addWidget(self.resStrike, 1, 1)
        self.leftInnerLayOut.addWidget(QLabel("Ball : "), 1, 2)
        self.leftInnerLayOut.addWidget(self.resBall, 1, 3)

        self.leftInnerLayOut.addWidget(QLabel("Probability : "), 2, 0)
        self.leftInnerLayOut.addWidget(self.probabilityRes, 2, 1)
        self.leftInnerLayOut.addWidget(self.hintBtn, 3, 0)
        self.leftInnerLayOut.addWidget(self.resetBtn, 3, 1)

        # leftGroupBox에 leftInnerLayOut 추가
        self.leftGroupBox.setLayout(self.leftInnerLayOut)

        # leftLayout이름의 BoxLayout 생성후 leftGroupBox 추가
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.leftGroupBox)

        # rightGroupBox이름의 GroupBox 생성
        self.rightGroupBox = QGroupBox("기록")

        # rightInnerLayOut이름의 BoxLayout 생성
        self.rightInnerLayOut = QVBoxLayout()

        # rightInnerLayOut에 추가할 tableWidget이름의 TableWidget 생성후 세팅
        self.rightTableWidget = QTableWidget(10, 3)
        self.rightTableWidget.setHorizontalHeaderLabels(["Number", "Strike", "Ball"])
        self.rightTableWidget.resizeColumnsToContents()
        self.rightTableWidget.resizeRowsToContents()
        self.row = 0  # 기록의 row의 개수를 기록하기 위한 변수

        # rightInnerLayOut 안에 righttableWidget 추가
        self.rightInnerLayOut.addWidget(self.rightTableWidget)

        # rightGroupBox에 rightInnerLayOut 추가
        self.rightGroupBox.setLayout(self.rightInnerLayOut)

        # rightLayout이름의 BoxLayout 생성후 rightGroupBox 추가
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.rightGroupBox)

        # bottomGroupBox이름의 GroupBox 생성
        self.bottomGroupBox = QGroupBox("힌트")

        # bttomInnerLayout이름의  BoxLayout 생성
        self.bottomInnerLayout = QVBoxLayout()

        # bottomInnerLayOut에 추가할 tableWidget이름의 TableWidget 생성후 세팅
        self.bottomTableWidget = QTableWidget(40, 10)
        self.bottomTableWidget.resizeColumnsToContents()
        self.bottomTableWidget.resizeRowsToContents()

        # bottomInnerLayout 안에 bottomTableWidget 추가
        self.bottomInnerLayout.addWidget(self.bottomTableWidget)

        # bottomGroupBox에 bottomInnerLayout 추가
        self.bottomGroupBox.setLayout(self.bottomInnerLayout)

        # bottomLayout이름의 BoxLayout 생성후 bottomGroupBox 추가
        self.bottomLayout = QVBoxLayout()
        self.bottomLayout.addWidget(self.bottomGroupBox)

        self.outLayout = QVBoxLayout()
        #
        self.contentHLayout = QHBoxLayout()
        self.contentHLayout.addLayout(self.leftLayout)
        self.contentHLayout.addLayout(self.rightLayout)

        #
        self.contentVLayout = QVBoxLayout()
        self.contentVLayout.addLayout(self.bottomLayout)

        self.outLayout.addLayout(self.contentHLayout)
        self.outLayout.addLayout(self.contentVLayout)

        self.setLayout(self.outLayout)

        # 확인 버튼 이벤트 호출
        self.submitBtn.clicked.connect(self.submitBtnListener)
        # 힌트 받기 버튼 이벤트 호출
        self.hintBtn.clicked.connect(self.hintBtnListener)
        # 리셋 버튼 이벤트 호출
        self.resetBtn.clicked.connect(self.resetBtnListener)

        self.oldRow = 0
        self.newRow = 40

    def submitBtnListener(self):
        print("확인 버튼 호출")
        if self.row == 4:
            print("10번 입력 초과")
            QMessageBox.information(self, "김형근", "넌... 패배자다....")
            QMessageBox.information(self, "김형근", "한번 더 할거냐? \n김형근 : 쫄? 쪼오올~??")
        else:
            tempNum = self.inputNumber.text()
            # 여기 입력 예외처리 해야함
            firstNum = int(tempNum) / 100
            secondNum = int(tempNum) % 100 / 10
            thirdNum = int(tempNum) % 100 % 10

            res = self.mydll.playball(int(firstNum), int(secondNum), int(thirdNum))
            print("랜덤 값 : ", self.rand)
            resList = [i for i in res.contents]
            print("Strike : ", resList[0], "Ball : ", resList[1])
            self.resStrike.setText(str(resList[0]))
            self.resBall.setText(str(resList[1]))
            self.rightTableWidget.setItem(self.row, 0, QTableWidgetItem(str(tempNum)))
            self.rightTableWidget.setItem(self.row, 1, QTableWidgetItem(str(resList[0])))
            self.rightTableWidget.setItem(self.row, 2, QTableWidgetItem(str(resList[1])))
            self.row += 1

    def hintBtnListener(self):
        print("힌트 받기 버튼 호출")
        count = 0
        tempNum = self.inputNumber.text()
        firstNum = int(tempNum) // 100
        secondNum = int(tempNum) % 100 // 10
        thirdNum = int(tempNum) % 100 % 10
        print(tempNum)
        res = self.mydll.hint(int(firstNum), int(secondNum), int(thirdNum), int(self.resStrike.text()),
                              int(self.resBall.text()))
        resList = [i for i in res.contents]
        self.bottomTableWidget.clear()
        for i in resList:
            if i != -1:
                # print(i)
                self.oldRow = self.newRow
                self.newRow = count // 10
                self.bottomTableWidget.setItem(self.newRow, count % 10, QTableWidgetItem(str(i)))
                # self.bottomTableWidget.rowResized(self.oldRow,self.oldRow,self.newRow)
                # self.bottomTableWidget.resizeRowToContents(int(count // 10))

                count += 1

    def resetBtnListener(self):
        print("리셋 버튼 호출")
        self.mydll = ctypes.windll.LoadLibrary('C:\Huni_Project\Pycharm_Project\pyqt5_Project\Dll2.dll')
        self.mydll.datainit.restype = ctypes.c_int  # c라이브러리의 datainit()함수의 리턴타입 지정
        self.rand = self.mydll.datainit()

        self.mydll.playball.argtype = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.mydll.playball.restype = ctypes.POINTER(ctypes.c_int * 2)

        self.mydll.hint.argtype = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.mydll.hint.restype = ctypes.POINTER(ctypes.c_int * 999)

        self.inputNumber.clear()
        self.resStrike.clear()
        self.resBall.clear()
        self.rightTableWidget.clear()
        self.bottomTableWidget.clear()
        self.row = 0


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 프로그램 환경 세팅
        self.setWindowTitle('NumberBaseBall - Create By [Huni]')
        self.setWindowIcon(QIcon('icon/baseball.png'))
        self.setGeometry(-800, 600, 520, 380)
        self.contentWidget = Content()  # MainWindow는 자체적으로 layout을 가지고 있다. 위젯의 인스턴스 생성만으로도 QMainWindow에 붙는다.
        self.setCentralWidget(self.contentWidget)  # 그래서 setCentralWidget()로 widget을 추가해주면 된다.

        # 메뉴바의 정보
        infoAction = QAction(QIcon('info.png'), 'info', self)
        infoAction.setShortcut('Ctrl+I')
        infoAction.setStatusTip('dev info')
        infoAction.triggered.connect(self.menu_info)  # 메뉴바의 info를 클릭했을때 menu_info()함수 호출

        # 메뉴바의 종료
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # 메뉴바 생성
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(infoAction)
        filemenu.addAction(exitAction)

    def menu_info(self):
        QMessageBox.information(self, "info",
                                '안녕! 공부하면서 숫자야구게임으로 한번 만들어 봤어!\n\nE-mail - 91huniya@gmail.com\ngit - https://github.com/huni1153')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
