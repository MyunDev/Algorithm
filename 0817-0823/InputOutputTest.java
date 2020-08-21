import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class InputOutputTest {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		//Scanner를 사용했을시 입력 형태.
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		// AB CDD EFFF GH 입력

	String a = st.nextToken(); // AB
	String b = st.nextToken();// CDD
	String c = st.nextToken(); // EFFF
	String d = st.nextToken(); // GH
	
	System.out.println(a);
	System.out.println(b);
	System.out.println(c);
	System.out.println(d);
	}

}
