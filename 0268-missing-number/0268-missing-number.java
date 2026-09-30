class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expected = n * (n + 1) / 2;
        int actual = 0;
        for (int num : nums) {
            actual += num;
        }
        return expected - actual;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {3, 0, 1};
        System.out.println(sol.missingNumber(nums));
    }
}
