class Controller
{
    AdressMember am;

    컨트롤러는 스테틱으로 생성자로 초기화 했었나 ?

    추가하기 메소드()
        am.addToPerson()

    이름 수정하기 메소드(식별키 이름)
        am.nameModify()

    나이 수정하기 메소드(식별키 나이)
        am.ageModify()

    번호 수정하기 메소드(식별키 번호)
        am.telModify()

    이름으로 검색하기 메소드(이름)
        am.searchToName()

    나이로 검색하기 메소드(나이) //
        am.searchToAge()

    번호로 검색하기 메소드(번호)
        am.searchToTel()

    이름으로 삭제하기 메소드(이름)
        am.deleteToName()

    나이로 삭제하기 메소드(나이) // 근데 이거 나이가 같은 사람이 한둘이야?
        am.deleteToAge()

    번호로 삭제하기 메소드(번호)
        am.deleteToTel()


}