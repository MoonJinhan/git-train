
public class StringTest {

	public static void main(String[] args) {
		 // Character VS String 
        System.out.println("Hello World"); // String
        //자바에서는 "" , '' 이 두가지를 구별을 한다. 
        System.out.println('H'); // Character
        //''는 Character를 나타낸다. 한 글자를 표현하는 데이터 타입
        System.out.println("H"); 
        //""는 Character들이 모여있는 데이터 타입. == String 에서 사용
        System.out.println("Hello "
                + "World");
        //줄바꿈의 시도 하지만 실패..
        // new line
        System.out.println("Hello \nWorld");
        
        // \n을 사용하게 되면 한 줄을 뛰어서 쓰게 된다. 
        // escape
        System.out.println("Hello \"World\"");// Hello "World"
        // 역슬레쉬를 넣어주면 특수문자를 넣어주기 위해서 넣어준다.
	}

}
