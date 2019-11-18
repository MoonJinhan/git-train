## REST

Representational State Transfer 

**Roy Fielding** 논문으로 아키 텍쳐 발표

- Http 설계의 우수성에 비해 제대로 활용하고 있지 않아 빌



**HTTP**

- request/response 로 써버와 클라이언트간에 HTTP로 통신



웹서버는 웹 리소스를 관리하고 제공을 함.

1. 미디어 타입 : 수천가지 데이터 타입이 존재

**MIME(**Multipurpose Internet Mail Extensions)

**HTML**: text/html

**jpeg** : image/jpeg

**ASCII** : text/plain



2. **URI(URL+URN**)

URL : location 리소스의 위치 (스킵://서버위치/경로) 스킴 : 리소스에 접근하기 위한 프로토콜

URN : 위치에 독립적임.



### REST의 구성 

자원 : URL

행위 : HTTP Method(GET/POST/PUT/DELETE/)

표현 : 



#### REST 디자인 가이드

'/'눈 계층 관계를 나타내는데 사용

'_' 대신 '-' 를 활용

정보의 자원ㅇ르 표현해야함.



GET /boards/show/1 show라는 행위가 있기때문에 REST하지 않음

GET /boards/1



GET /boards/create (REST X)

POST /boards

django : POST/boards/1/edit



GET /boards/1/update (REST X)

PUT /boards/1





GET /boards/1/delete (REST X)

DELETE/boards/1



django 에서는 Http method 를 GET/POST 만 제공함.



boards/new

데이터를 생성하기위한 폼을 불러오는 거기 때문에 GET

boards/create

데이터를 생성을 하기 때문에 POST





