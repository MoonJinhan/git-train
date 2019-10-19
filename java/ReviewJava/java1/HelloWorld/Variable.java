
public class Variable {
	public static void main(String[] args) {
		
		//a = 1; 변수를 정해 줄 때, 자바에서는 타입을 지정해 줘야한다.
		int a = 1;
		System.out.println(a);
		
		//int b = 1.1; 에러가 벙 하고 나오는데 int 에는 정수만 들어갈 수만 있다. 
		//1.1은 실수에 들어가 있기 때문에 이에 맞는 타입을 지정해 줘야한다.(double)
		double b = 1.1;
		System.out.println(b);
		
		String c="Hello World";
		System.out.println(c);
		
		//이렇게 해주는 변수를 생성할 때 마다 타입을 지정해주는 이유는 
		//우리가 변수가 어떤 타입인지 확인하는 절차를 생략해 줄 수 있기 때문이다.
		//예를 들어서(자바야학에서 나온 예)어떤 액체가 들어있는 페트병이 있다.
		//그런데 뚜껑이 따져있고 우리는 이것을 마실지, 안 마실지 고민을 해야한다.
		//즉, 그런데 옆에 물 컵이 있어서 아! 물이 안에 들어 갔구나.
		//하게 되면 우리는 그제서야 페트병에 들어 있는 것이 물이라고 생각을 하고
		//마신다. 
	}

}
