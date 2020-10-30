class AdressMember
{
    List<Person> personList;

    AdressMember()
    {
        List<Person> personList = new ArrayList<Person>();
    }
    addToPerson(식별키 이름 나이 번호)
    {
        person 객체 생성 후 리스트에 append;
    }
    // 수정
    personModify(식별키 이름 나이 번호) 모든 정보 수정하는 메소드
    {
        식별키로 리스트내의 person객체에 접근해 받아온 이름 나이 번호를 식별키의 person객체 수정
    }
    nameModify(식별키 이름)
    {
        식별키로 리스트내의 person객체에 접근해 받아온 이름 수정
    }
    ageModify(식별키 나이)
    {
        위랑 같음
    }
    telModify(식별키 번호)
    {
        위랑 같음
    }
    이름이랑 나이만 수정하는 메소드(식별키 이름 나이)

    나이랑 번호만 수정하는 메소드(식별키 나이 번호)

    이름이랑 번호만 수정하는 메소드(식별키 이름 번호)

    // 검색
    searchToName(이름)
    {
        받아온 이름으로 리스트내의 person객체에 접근해 모든 이름 출력
    }
    searchToAge(나이)
    {
        리스트 내의 받아온 나이를 모두 출력
    }
    searchToTel(번호)
    
    // 삭제
    deleteToName(이름)
    {
        받아온 이름으로 리스트내의 person객체에 접근해 모든 이름에 해당하는 객체 삭제
    }
    deleteToAge(나이)
    {
        해당 나이를 리스트내의 객체에 접근해 모든 나이에 해당하는 객체 삭제
    }
    deleteToTel(전화번호)
    {
        번호는 유일하니 하나만 삭제하겠지?
    }
    
}