class Solution {
    public int[] shuffle(int[] nums, int n) {
        int x = 0;
        int y = n;
        int arr[] = new int[2*n];
        for (int i = 0; i < arr.length; i+=2){
            arr[i] = nums[x++];
            arr[i+1] = nums[y++];
        }return arr;
        
    }
}