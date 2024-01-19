import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
		int x = Integer.parseInt(rd.readLine());
		int y = Integer.parseInt(rd.readLine());
		System.out.println(x*(y%10));
		System.out.println(x*(y/10%10));
		System.out.println(x*(y/100%10));
		System.out.println(x*y);
	}
}