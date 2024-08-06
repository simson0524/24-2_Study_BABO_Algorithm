import java.io.BufferedReader;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;

import java.io.OutputStreamWriter;
import java.util.Arrays;

import java.util.HashMap;

import java.util.StringTokenizer;


public class Main {

	public static HashMap<Integer, Integer> map = new HashMap<>();

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(bf.readLine());

		StringTokenizer st = new StringTokenizer(bf.readLine());

    // 입력 받을 배열
		int [] arr = new int[n];
		// 정렬할 배열
    int [] sortedArr = new int[n];
		// 출력할 배열
    int [] result = new int[n];

		for(int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

    // 배열 복사
		System.arraycopy(arr, 0, sortedArr, 0, n);

    // 오름차순 정렬
		Arrays.sort(sortedArr);
  
		for(int i = 0; i < n; i++) {
			if(!map.containsKey(sortedArr[i])) {
				map.put(sortedArr[i], map.size()); // map.size를 통해 고유번호를 지정해서 rank를 만듬 (그냥 인덱스 i를 사용하면 정렬된 배열에서 중복값을 고려하게 됨)
			}
		}

    // 입력 받은 배열을 map에서 rank를 찾아 결과를 출력할 배열에 저장
		for(int i = 0; i < n; i++) {
			result[i] = map.get(arr[i]);
		}

		for(int i = 0; i < n; i++) {
			bw.write(String.valueOf(result[i]) + " ");
		}

		bw.close();

	}
}
