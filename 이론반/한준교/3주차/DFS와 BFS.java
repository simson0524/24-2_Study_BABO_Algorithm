import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, m ,v;
    static ArrayList<Integer> [] arr;
    static boolean [] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        arr = new ArrayList[n + 1];

        // 정점이 1부터 시작하니까 index도 맞춰줌
        for(int i = 1; i < n + 1; i++)
            arr[i] = new ArrayList<Integer>();

        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            arr[a].add(b);
            arr[b].add(a);
        }

        // 낮은 숫자부터 방문하기 위해 arr을 정렬함
        for (int i = 1; i < n + 1; i++) {
            Collections.sort(arr[i]);
        }

        visited = new boolean[n + 1];
        dfs(v);

        System.out.println();

        visited = new boolean[n + 1];
        bfs(v);

    }
    
    public static void dfs(int start) {
        System.out.print(start + " ");
        visited[start] = true; // 현재 노드를 방문했다고 표시해둠

        // 현재 노드와 연결된 다른 노드들을 살펴봄
        for(int i : arr[start]) {
            
            // 방문하지 않았다면 재귀를 통해 해당 노드를 즉시 방문 (연결된 노드가 여러개여도 쭉 타고 들어가서 탐색)
            if(!visited[i])
                dfs(i);

        }

    }

    public static void bfs(int start) {

        ArrayDeque<Integer> toVisit = new ArrayDeque<>(); // 앞으로 방문해야 할 노드

        toVisit.add(start); 

        // toVisit에 아무것도 남지 않을 때까지 반복
        while(!toVisit.isEmpty()) {
            // FIFO
            int a = toVisit.pop();
            System.out.print(a + " ");
            visited[a] = true; // 현재 노드를 방문했다고 표시함

            // 현재 노드와 연결된 다른 노드들을 하나씩 살펴봄
            for(int i = 0; i < arr[a].size(); i++) {
                int b = arr[a].get(i);

                // 방문했던 노드가 아니라면 실행할 작업
                if(!visited[b]) {
                    visited[b] = true; // 방문할 노드에 추가했으므로 (pop에 의해 실행이 될 것이므로) 방문했다고 표시해서 toVisit에 중복된 값이 들어가지 않게 함
                    toVisit.add(b); // 앞으로 방문할 노드에 추가
                }
            }
        }
    }
}
