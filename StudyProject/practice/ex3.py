strTmp = '''
class Person():

    def __init__(self, name, age, local, think):
        self.name = name
        self.age = age
        self.local = local
        self.think = think
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_local(self):
        return self.local
    def get_think(self):
        return self.think
        
        
        
        
# psh = Person("박세훈","30살","서울") 생성자 오버로딩이 파이썬에는 없다..
# print(psh.get_name())
lkw = Person("이경원", "30살", "서울","그는 지금 집에 가고싶다.")
print(lkw.get_local())
'''

strQuest = '''
person 클래스 만들기
인스턴스변수 : 이름, 나이
person을 상속받는 content클래스
인스턴스변수 : 전화번호
container 클래스를 만들어서
클래스변수로 content(연락처)를 담는 빈 리스트를 만들자.
1. 생성
2. 수정
3. 삭제
4. 출력
5. 종료
'''



