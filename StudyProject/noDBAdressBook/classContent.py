from noDBAdressBook import classPerson


class Content(classPerson.Person):
    def __init__(self, name, age, tel):
        super().__init__(name, age)
        self.tel = tel

    def setTel(self, tel):
        self.tel = tel
    def getTel(self):
        return self.tel



