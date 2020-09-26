/*
Title:  Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.



Example 1:
Input: [10,2]
Output: "210"



Example 2:
Input: [3,30,34,5,9]
Output: "9534330"


Note: The result may be very large, so you need to return a string instead of an integer.

*/


class Solution {
    public String largestNumber(int[] nums) {
        if (nums == null || nums.length == 0) {
            return "";
        }

        String[] stringArray = new String[nums.length];
        for (int i=0; i<nums.length; i++) {
            stringArray[i] = Integer.toString(nums[i]);
        }

        Arrays.sort(stringArray, new Comparator<String>() {
            public int compare(String s1, String s2) {
                String option1 = s1 + s2;
                String option2 = s2 + s1;
                return option2.compareTo(option1);
            }
        });

        if (stringArray[0].equals("0")) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for (String str : stringArray) {
            sb.append(str);
        }

        return sb.toString();
    }
}
