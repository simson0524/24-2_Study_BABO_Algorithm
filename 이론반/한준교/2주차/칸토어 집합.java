import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input;
    
    // EOF 에서 parseInt로 인한 Number format 런타임 에러 방지를 위해 null 확인
		while((input = br.readLine()) != null) {
			int n = Integer.parseInt(input);
			Cantor(n);
			System.out.println();
		}
	}


	public static void Cantor(int n) {
		// 3^0 (=1) 이면 "-" 출력하고 종료
    if(n == 0)
			System.out.print("-");
		else {
			Cantor(n-1); // 3등분 했을 때 하나의 그룹으로 생각하면 3^n / 3 만큼 다시 똑같은 작업을 반복 => 3^n-1 즉 n-1을 넘겨주어 재귀를 실행
			System.out.print(" ".repeat((int)Math.pow(3, n - 1))); // 3등분이므로 3^n / 3 만큼 가운데가 지워짐 => 3^n-1 만큼 공백으로 매꿈
			Cantor(n-1); // 3등분 했을 때 하나의 그룹으로 생각하면 3^n / 3 만큼 다시 똑같은 작업을 반복 => 3^n-1 즉 n-1을 넘겨주어 재귀를 실행
		}
	}
}
