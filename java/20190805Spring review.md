# Spring review



> 스프링의 기본 예제를 잘 정리해주셔서  이를 통해서 공부를 합니다.
>
> 목표 : 스프링의 기본적인 흐름과 사용법을 숙지합니다.
>
> (내용은 아래의 링크를 타고 공부를 하시면 좋을 것 같고, 제가 모르는 용어정리를 하면서 리뷰를 합니다. 그리고 집에가서 생각을 하면서)



#### 어노테이션 정리



** http://www.libqa.com/wiki/107 **



### @Controller

: 클래스가 컨트롤러라는 것을 스프링에 알려주는 용도.

### @requestMapping

: 클라이언트는 URL로 요청을 전송 그리고 요청  URL을 어떤 메서드가 처리할지 여부를 경절정하는 역할![rrequestmapping](C:\Users\user\Desktop\공부\코딩\spring\어노테이션\rrequestmapping.PNG)

출처: https://mrrootable.tistory.com/75



### @RequestParam

: 파라미터 값을 갖고 온다.



![rquestParameter](C:\Users\user\Desktop\공부\코딩\spring\어노테이션\rquestParameter.PNG)

위으 이미지는 @requestparam 을 사용하기전에 getParameter 를 이용해서 파라미터값을 가지고 온 것을 볼 수 있다.  그리고 아래의 이미지는 @requestParam을 이용해서 여러 타입과 그에 따른 값들을 가지고오는 어노테이션,옵션값등을 나타낸다.

![@requestparam](C:\Users\user\Desktop\공부\코딩\spring\어노테이션\@requestparam.PNG)



### @Autowired

: 스프링이 빈의 요구 사항과 매칭 되는 애플리케이션 컨텍스트상에서 다른 빈을 찾아 빈 간의 의존성을 자동으로 만족시키도록 하는 수단이다.



```
예제1

package demo; 
import org.springframework.beans.factory.annotation.Autowired; 
import org.springframework.stereotype.Component; 

@Component 
	public class CDPlayer implements MediaPlayer{ 
        @Autowired 
       		 private CompactDisc cd; 
       		 }

예제2

package demo; 
import org.springframework.beans.factory.annotation.Autowired; 
import org.springframework.stereotype.Component; 

    @Component 
    public class CDPlayer implements MediaPlayer{ 
        //@Autowired 
        	private CompactDisc cd; 
        	
            @Autowired public CDPlayer(CompactDisc cd) { 
           			 this.cd = cd; 
            } 
    }

출처: https://tbang.tistory.com/87 [heene]
```





###  Iterator 타입

: iterator 는 자바의 컬랙션 프레임 웍에서 컬랙션에 저장되어 있는 요소를 읽어오는 방법을 표준화 한 것이다. 



~~~
public interface Iterator {

    boolean hasNext();
    // 이 메소드는 읽어 올 요소가 남아있는지 확인하는 메소드이다.
    Object next();
    void remove();

    }


출처: https://vaert.tistory.com/108 [Vaert Street]
~~~



### 스프링 구조와 방식

> 스프링을 만드는데 필요한 재료들을 설정하고, 파악하기.
>
> 참고한 블로그
>
> :  https://addio3305.tistory.com/72 
>
> : https://blog.outsider.ne.kr/913
>
> :https://m.blog.naver.com/scw0531/220988401816



**Controller - service - serviceimpl - dao - sql - jsp**



#### 1. 구현할 링크 만들기

#### 2. 메인 페이지 메핑

#### 3. 회원의 정보를 담을 테이블 생성

#### 4. 생성자들을 생성  ex: signupVO

#### 5. 회원가입 controller 제작

 1. 회원가입 인터페이스 설정

 2. 회원가입 serviceimpl 생성 : serviceimpl 은 위에서 생성된 인터페이스를 실제로 구현한 것.

 3. 회원가입  DAO interface 생성

 4. 회원가입 DAOImpl 생성

    

