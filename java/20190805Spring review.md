# Spring review



> 스프링의 기본 예제를 잘 정리해주셔서  이를 통해서 공부를 합니다.
>
> 목표 : 스프링의 기본적인 흐름과 사용법을 숙지합니다.
>
> (내용은 아래의 링크를 타고 공부를 하시면 좋을 것 같고, 제가 모르는 용어정리를 하면서 리뷰를 합니다. 그리고 집에가서 생각을 하면서)



### 어노테이션 정리



** http://www.libqa.com/wiki/107 **



#### @Controller

: 클래스가 컨트롤러라는 것을 스프링에 알려주는 용도.

#### @requestMapping

: 클라이언트는 URL로 요청을 전송 그리고 요청  URL을 어떤 메서드가 처리할지 여부를 경절정하는 역할





출처: https://mrrootable.tistory.com/75



#### @RequestParam

: 파라미터 값을 갖고 온다.





위으 이미지는 @requestparam 을 사용하기전에 getParameter 를 이용해서 파라미터값을 가지고 온 것을 볼 수 있다.  그리고 아래의 이미지는 @requestParam을 이용해서 여러 타입과 그에 따른 값들을 가지고오는 어노테이션,옵션값등을 나타낸다.





#### @Autowired

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







## 스프링 구조와 방식

> 스프링을 만드는데 필요한 재료들을 설정하고, 파악하기.
>
> 참고한 블로그
>
> :  https://addio3305.tistory.com/72 
>
> : https://blog.outsider.ne.kr/913
>
> :https://m.blog.naver.com/scw0531/220988401816
>
> :https://debugdaldal.tistory.com/127
>
> 

### web.xml

> 설정을 위한 설정파일이다. 배포 기술자로써 영어로는 DD(Deployment Descriptor) 이다. 이 파일은 WAS(Web Application Server)가 최초 구동될 때 즉 톰켓이 최초 구동될 때 web.xml을 읽고 그에 해당하는 설정을 구성한다. 즉 각종 설정을 위한 설정파일이라고 할 수 있다.

```xml

<?xml version="1.0" encoding="UTF-8"?>
<web-app version="2.5" xmlns="http://java.sun.com/xml/ns/javaee"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">
      <!-- The definition of the Root Spring Container shared by all Servlets and Filters -->
      <context-param>  - 루트 컨텍스트로 모든 서블릿과 필터들이 공유함. root-context.xml을 정의
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/spring/root-context.xml</param-value>
      </context-param>
      
      <!-- Creates the Spring Container shared by all Servlets and Filters -->
      <listener> - 리스너로써 루트 컨텍스트에 정의 되어있는 것들을 모든 서블릿과 필터가 공유할 수 있게 해준다고 함.
            <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
      </listener>
      <!-- Processes application requests -->
      <servlet> - 서블릿 설정
            <servlet-name>appServlet</servlet-name>
            <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class> - DispatcherServlet으로 앞단에서 요청정보를 핸들링 해줌.
            <init-param>
                  <param-name>contextConfigLocation</param-name> 
                  <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value> -servlet-context.xml을 가르키고 있음.
            </init-param>
            <load-on-startup>1</load-on-startup>
      </servlet>
            
      <servlet-mapping> - appServlet에 대한 url-pattern을 정의
            <servlet-name>appServlet</servlet-name>
            <url-pattern>/</url-pattern>
      </servlet-mapping>
</web-app>


출처: https://debugdaldal.tistory.com/127 [달달한 디버깅]
```



###  servlet-context.xml

> 주석을 보면  <!-- DispatcherServlet Context: defines this servlet's request-processing infrastructure --> 이라고 나와있다. 해석해보면 DispatcherServlet Context : 이 서블릿의 요청처리 인프라를 정의한다. 이다. Dispatcher 서블릿과 관련된 설정을 하는것 같다.
>
> 정답은 아니지만 주로 View 지원 bean을 설정한다고 한다. ex) Controller
> 그래서 그런지 어노테이션, 리소스 디렉토리, ViewResolver에 관한 설정들이 있다.



```xml


<?xml version="1.0" encoding="UTF-8"?>
<beans:beans xmlns="http://www.springframework.org/schema/mvc"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:beans="http://www.springframework.org/schema/beans"
      xmlns:context="http://www.springframework.org/schema/context"
      xsi:schemaLocation="http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc.xsd
            http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
      <!-- DispatcherServlet Context: defines this servlet's request-processing infrastructure -->
      
      <!-- Enables the Spring MVC @Controller programming model -->
      <annotation-driven /> - 어노테이션을 사용한다고 선언
      <!-- Handles HTTP GET requests for /resources/** by efficiently serving up static resources in the ${webappRoot}/resources directory -->
      <resources mapping="/resources/**" location="/resources/" /> - HTML 리소스 디렉토리 정의
      <!-- Resolves views selected for rendering by @Controllers to .jsp resources in the /WEB-INF/views directory -->
      <beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver"> - ViewResolver로 jsp와 name 을 매핑
            <beans:property name="prefix" value="/WEB-INF/views/" />
            <beans:property name="suffix" value=".jsp" />
      </beans:bean>
      
      <context:component-scan base-package="com.hee.heechart" /> - 베이스 패키지 하위 모든 어노테이션을 스캔해서 빈으로 등록하겠다는 것.
     
</beans:beans>


출처: https://debugdaldal.tistory.com/127 [달달한 디버깅]
```



### root-context.xml 

처음에 프로젝트 생성시에는 아무 내용도 없다. 이곳은 공통빈을 설정하는 곳으로 주로 View 지원을 제외한 bean을 설정한다고 한다.

ex) Service / Repository(DAO) / DB/ log 등등





#### 1. 구현할 링크 만들기

#### 2. 메인 페이지 메핑

#### 3. 회원의 정보를 담을 테이블 생성

#### 4. 생성자들을 생성  ex: signupVO

#### 5. 회원가입 controller 제작

 1. 회원가입 인터페이스 설정

 2. 회원가입 serviceimpl 생성 : serviceimpl 은 위에서 생성된 인터페이스를 실제로 구현한 것.

 3. 회원가입  DAO interface 생성

 4. 회원가입 DAOImpl 생성

    

