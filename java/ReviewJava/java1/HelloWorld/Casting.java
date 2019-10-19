
public class Casting {
	public static void main(String[] args) {
		
		 	double a = 1.1;
	        double b = 1;
	        
	        //실수가 아니더라도 에러는 나지 않는다.(자도)
	        double b2 = (double) 1;
	        //위에는 b와 같은 결과를 나타내지만 수동으로 한다고 생각하면 된다.
	        System.out.println(b);
	        //출력이 1.0 실수로 출력이 된다. 즉 컨버팅이 된다.
	        
	        // int c = 1.1; 에러. 만약 자동으로 실수가 정수로 바뀐다면
	        //0.1을 잃어버릴 수가 있다. 그래서 이를 방지하기 위해서 에러.
	        //이를 "손실"이라고 부른다.
	        
	        System.out.println(b2);
	        //
	        int e = (int) 1.1;
	        //인티저(정수)인데 강제로 더블로 나타내겠다다. 할 때 저렇게 작성.
	        System.out.println(e);
	         
	        // 1 to String 
	        String f = Integer.toString(1);
	        System.out.println(f.getClass());
	 
	 
	}

}
