# Review



#### model

- class명이 table 명
- class 변수가 column명
- 클래스 메소드로 __str__()재정의
  - 데이터가 잘 저장됬는지 확인차.

#### makemigrations

- 장고에서 변경된 부분으 ㄹ migrations 폴더안에 0001같이 명세서를 작성.
- 혹시, 오타면 마이그레이션 파일은 순정하지 말고, 마이크레이션 파일은 수정하지 말고 models.py를 수정. 장고에서 벼경점을 못 찾을  때는 새롭게 생성된 migration 파일 삭제

#### migrate

- migration 파일을 바탕으로 BD에 테이블을 적용

#### Admin.py

- DB관리용 페이지
- 일반 사용자에게 보여지는 페이지는 아니고, 괄리를 위한 페이지 !
- feilds list, tuple현식으로 수정할 항목이나 순서를 설정을 했음
  - 주의: auto_now=True 설정시, editable=False 로 자동 설정되서 fields에서 사용할 수 없음
- list_filter:bool , char,date, datetime,integer ~속성만 필터링 가능