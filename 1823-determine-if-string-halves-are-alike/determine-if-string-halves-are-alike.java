class Solution {
    public boolean halvesAreAlike(String s) {
        int count1 = 0;
        int count2 = 0;

        for (int i = 0; i < s.length() / 2; i++) {
            char ch = s.charAt(i);
            if (ch == 'a' || ch == 'A' ||
                ch == 'e' || ch == 'E' ||
                ch == 'i' || ch == 'I' ||
                ch == 'o' || ch == 'O' ||
                ch == 'u' || ch == 'U') {
                count1++;
            }
        }

        for (int i = s.length() / 2; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == 'a' || ch == 'A' ||
                ch == 'e' || ch == 'E' ||
                ch == 'i' || ch == 'I' ||
                ch == 'o' || ch == 'O' ||
                ch == 'u' || ch == 'U') {
                count2++;
            }
        }

        return count1 == count2;
    }
}