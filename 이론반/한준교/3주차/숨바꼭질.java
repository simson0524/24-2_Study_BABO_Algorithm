import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {
    static int n, k;
    static int [] cnt;
    static boolean[] visited;
    static final int max = 100001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        // 방문할 수 있는 최대 노드 수로 설정
        visited = new boolean[max];
        cnt = new int[max];
        find(n);
        System.out.println(cnt[k]);
    }

    public static void find(int start) {
        Queue<Integer> toVisit = new LinkedList<>();
        toVisit.add(start); // 방문해야할 노드에 추가
        visited[start] = true;

        while(!toVisit.isEmpty()) {

            int now = toVisit.poll();

            // 동생 위치에 도착했으면 현재 위치의 cnt값 반환
            if(now == k)
                return;

            if(now - 1 >= 0 && !visited[now -1]) {
                toVisit.add(now - 1); // 다음 방문할 위치에 추가
                cnt[now - 1] = cnt[now] + 1; // 다음 방문할 위치의 cnt 값을 증가 (현재 위치에서 한 번 이동해야 다음 방문 위치에 도달하므로)
                visited[now - 1] = true; // visited에 추가
            }

            if(now + 1 < max && !visited[now + 1]) {
                toVisit.add(now + 1);
                cnt[now + 1] = cnt[now] + 1;
                visited[now + 1] = true;
            }

            if(now * 2 < max && !visited[now * 2]) {
                toVisit.add(now * 2);
                cnt[now * 2] = cnt[now] + 1;
                visited[now * 2] = true;
            }
        }
    }

}
