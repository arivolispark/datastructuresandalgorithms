import java.util.Map;
import java.util.HashMap;

public class Question_1_TwoSum {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        System.out.println("\n Display input nums");
        displayIntArray(nums);

        System.out.println("\n target: " + target);

        int[] twoSumArray = twoSum(nums, target);
        System.out.println("\n Display twoSumArray");
        displayIntArray(twoSumArray);
    }

    private static void displayIntArray(int[] intArray) {
        if (intArray == null) {
            System.out.println("\n input array is null");
        } else if (intArray.length == 0) {
            System.out.println("\n input array is of length zero");
        } else {
            for (int i=0; i<intArray.length; i++) {
                System.out.println(" intArray[" + i + "]: " + intArray[i]);
            }
        }
    }

    public static int[] twoSum(int[] nums, int target) {
        int[] result = null;
        int[] targetNums = null;
        Map<Integer, Integer> sourceMap = null;

        if (nums != null && nums.length > 0) {
            targetNums = new int[nums.length];
            sourceMap = new HashMap<Integer, Integer>();

            for (int i=0; i<nums.length; i++) {
                targetNums[i] = target - nums[i];
                sourceMap.put(nums[i], i);
            }
            System.out.println("\n sourceMap: " + sourceMap);

            System.out.println("\n Display targetNums");
            displayIntArray(targetNums);

            for (int i=0; i<targetNums.length; i++) {
                if (sourceMap != null && !sourceMap.isEmpty()) {
                    Integer complementaryNum = sourceMap.get(targetNums[i]);
                    if (complementaryNum != null) {
                        result = new int[2];
                        result[0] = i;
                        result[1] = complementaryNum;
                        break;
                    }
                }
            }
        }

        return result;
    }
}