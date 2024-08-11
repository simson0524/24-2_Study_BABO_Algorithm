import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int l, c;
    static char [] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st1 = new StringTokenizer(br.readLine());

        l = Integer.parseInt(st1.nextToken());
        c = Integer.parseInt(st1.nextToken());

        st1 = new StringTokenizer(br.readLine());

        arr = new char[c];

        for(int i = 0; i < c; i++) {
            arr[i] = st1.nextToken().charAt(0);
        }

        Arrays.sort(arr); // 입력받은 알파벳을 미리 오름차순 정렬하여 앞에서 부터 차례로 확인 (암호가 오름차순인지 확인할 필요가 없어짐)

        find(0, "", 0, 0); // index 는 0부터 시작, 빈 문자열부터 차례로 채움, 포함된 모음/자음 개수 0개부터 시작

    }

    public static void find(int index, String result, int aeiou, int other) {

        // 모든 경우를 다 구해서 마지막 index에 도달했을 경우
        if(index == c) {
          // 모음이 1개이상, 자음이 2개이상, 주어진 암호 개수가 일치하는지 확인하고 일치하면 출력
            if(aeiou >= 1 && other >=2 && result.length() == l) {
                System.out.println(result);
            }

            return;
        }

        if("aeiou".contains(Character.toString(arr[index]))) {
            aeiou++;
            find(index + 1, result + arr[index], aeiou, other); // 현재 확인하는 모음을 암호에 넣을 경우
            find(index + 1, result, aeiou-1, other); // 현재 확인하는 모음을 암호에 넣지 않을 경우
        } else {
            other++;
            find(index + 1, result + arr[index], aeiou, other); // 현재 확인하는 자음을 암호에 넣을 경우
            find(index + 1, result, aeiou, other-1); // 현재 확인하는 자음을 암호에 넣지 않을 경우
        }
    }
}
