package arrays;

public class MedianOfTwoSortedIntegerArrays {
    public static void main(String[] args) {
        int[] nums1 = new int[] {1, 3};
        int[] nums2 = new int[] {2, 4};

        System.out.println("\n Display nums1");
        display(nums1);

        System.out.println("\n Display nums2");
        display(nums2);

        double median = findMedianOfSortedArrays(nums1, nums2);
        System.out.println("\n median: " + median);
    }

    private static void display(int[] intArray) {
        if (intArray == null || intArray.length <= 0) {
            System.out.println("\n intArray is null or empty");
        } else {
            for (int i=0; i<intArray.length; i++) {
                System.out.println(" intArray[" + i + "]: " + intArray[i]);
            }
        }
    }

    public static double findMedianOfSortedArrays(int[] nums1, int[] nums2) {
        if (nums1 == null) {
            if (nums2 == null) {
                return 0;
            } else {
                return calculateMedian(nums2);
            }
        } else if (nums2 == null) {
            return calculateMedian(nums1);
        } else {
            int[] consolidatedSortedArray = sort(nums1, nums2);
            System.out.println("\n Display consolidatedSortedArray");
            display(consolidatedSortedArray);

            return calculateMedian(consolidatedSortedArray);
        }
    }

    private static int[] sort(int[] intArray1, int[] intArray2) {
        int[] consolidatedSortedArray = null;
        if (intArray1 != null && intArray2 != null) {
            consolidatedSortedArray = new int[intArray1.length + intArray2.length];

            int i = 0;
            int j = 0;
            int k = 0;

            while (i < intArray1.length) {
                if (j < intArray2.length) {
                    if (intArray1[i] <= intArray2[j]) {
                        consolidatedSortedArray[k++] = intArray1[i++];
                    } else {
                        consolidatedSortedArray[k++] = intArray2[j++];
                    }
                } else {
                    consolidatedSortedArray[k++] = intArray1[i++];
                }
            }

            while (j < intArray2.length) {
                consolidatedSortedArray[k++] = intArray2[j++];
            }
        }
        return consolidatedSortedArray;
    }

    private static double calculateMedian(int[] intArray) {
        double median = 0.0;

        if (intArray != null) {
            if (intArray.length == 0) {
                return 0;
            } else {
                if ((intArray.length % 2) != 0) {
                    int middleIndex = (intArray.length / 2) + 1;
                    median = intArray[middleIndex - 1];
                } else {
                    int middleIndex1 = (intArray.length / 2);
                    int middleIndex2 = (intArray.length / 2) + 1;
                    median = (double)(intArray[middleIndex1 - 1] + intArray[middleIndex2 - 1]) / 2;
                }
            }
        }

        return median;
    }
}