import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {

        Arrays.sort(g);
        Arrays.sort(s);

        int cookie = 0;
        int kid = 0;
        int count = 0;

        while (cookie < s.length && kid < g.length) {

            if (g[kid] > s[cookie]) {
                cookie++;
            }
            
            else if(g[kid] <= s[cookie]) {
                count++;
                kid++;
                cookie++;
            }

            
        }

        return count;
    }
}