import java.util.*;
public class Solution {
    public int solution(int[][] routes) {
        int cnt = 0;
        int position = -30001;

        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));

        for (int[] route : routes) {
            if (position < route[0]) {
                position = route[1];
                cnt++;
            }
        }

        return cnt;
    }
}