package leetcode;

import java.util.Arrays;

public class LeetCode1313 {

    public static int[] decompressRLElist(int[] nums) {
        int size = 0;

        for (int i=0; i<nums.length; i += 2) {
            size += nums[i];
        }

        int[] resultArray = new int[size];

        int i = 0;
        int j = 0;

        while (i < nums.length) {
            int frequency = nums[i];
            int value = nums[i + 1];

            for (int k=0; k<frequency; k++) {
                resultArray[j++] = value;
            }

            i += 2;
        }

        return resultArray;
    }

    public static void main(String[] args) {

        /**
         * Input: nums = [1,2,3,4]
         * Output: [2,4,4,4]
         */

        int[] inputArray = new int[] {1, 2, 3, 4};

        System.out.println("\n Input array");
        System.out.println(Arrays.toString(inputArray));

        int[] outputArray = decompressRLElist(inputArray);
        System.out.println("\n Output array");
        System.out.println(Arrays.toString(outputArray));
        System.out.println(" outputArray.length: " + outputArray.length);
    }
}
