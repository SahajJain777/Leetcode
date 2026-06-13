class Solution {
    public int numIdenticalPairs(int[] nums) {
        int arr[] = new int[101];
        arr[nums[0]]++;
        int count = 0;
        for(int i = 1; i < nums.length; i++){
            if(arr[nums[i]] > 0){
                count += arr[nums[i]];
            }
            arr[nums[i]]++;
        }return count;
    }
}