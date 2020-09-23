/*
Title: Majority Element II

Given an integer array of size n, find all elements that
appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.


Example 1:
Input: [3,2,3]
Output: [3]


Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

*/

class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int count1 = 0;
        int count2 = 0;

        Integer candidate1 = null;
        Integer candidate2 = null;

        for (int n : nums) {
            if (candidate1 != null && candidate1 == n) {
                count1++;
            } else if (candidate2 != null && candidate2 == n) {
                count2++;
            } else if (count1 == 0) {
                candidate1 = n;
                count1++;
            } else if (count2 == 0) {
                candidate2 = n;
                count2++;
            } else {
                count1--;
                count2--;
            }
        }

        List<Integer> result = new ArrayList<>();
        count1 = 0;
        count2 = 0;

        for (int n : nums) {
            if (candidate1 != null && candidate1 == n) {
                count1++;
            }

            if (candidate2 != null && candidate2 == n) {
                count2++;
            }
        }

        int p = nums.length;
        if (count1 > p/3) {
            result.add(candidate1);
        }

        if (count2 > p/3) {
            result.add(candidate2);
        }

        return result;
    }
}
