package datastructuresandalgorithms.arrays;

import java.util.Arrays;

/**
 * Created by arivolitirouvingadame on 3/13/17.
 *
 * Given an array of integers, find the minimum and maximum values from the integer array.
 */
public class ArrayMinMax {
    public static void main(String[] args) {
//        int[] inputArray = null;
//        int[] inputArray = {};
        int[] inputArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        if (inputArray == null) {
            System.out.println("\n inputArray is null.  Can not find min and max.");
            return;
        }

        System.out.println("\n\n Input array");
        System.out.println(Arrays.toString(inputArray));

        if (inputArray.length == 0) {
            System.out.println("\n inputArray is of size zero.  Can not find min and max.");
            return;
        }

        for (int i=0; i<inputArray.length; i++) {
            if (inputArray[i] < min) {
                min = inputArray[i];
            }

            if (inputArray[i] > max) {
                max = inputArray[i];
            }
        }

        //Time complexity:  O(n)

        System.out.println("\n min: " + min);
        System.out.println(" max: " + max);
    }
}
