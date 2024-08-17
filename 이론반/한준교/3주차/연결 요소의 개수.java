import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, m, cnt;
    static int [][] arr;
    static int [] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n + 1][n + 1]; // index 번호를 실제 입력값에 맞추기 위해 +1 해줌

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            arr[u][v] = 1;
            arr[v][u] = 1;
        }

        visited = new int[n + 1];

        // 노드들을 모두 돌며 이전에 탐색되지 않은 노드가 있다면 연결 요소의 개수를 하나 늘려주고 dfs로 연결된 노드들을 전부 탐색하며 visited에 추가해줌
        for(int i = 1; i < n + 1; i++) {
            if(visited[i] == 0) {
                cnt++;
                dfs(i);
            }
        }

        System.out.println(cnt);
    }

    public static void dfs(int start){

        visited[start] = 1; // 방문한 노드에 현재 값을 추가해줌

        for (int i = 1; i < n + 1; i++) {
            if (arr[start][i] == 1)
                if (visited[i] != 1)
                    dfs(i);

        }
    }
}
