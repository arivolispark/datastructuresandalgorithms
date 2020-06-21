/*
Title:  Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

1) "123"
2) "132"
3) "213"
4) "231"
5) "312"
6) "321"

Given n and k, return the kth permutation sequence.

Note:
1) Given n will be between 1 and 9 inclusive.
2) Given k will be between 1 and n! inclusive.


Example 1:
Input: n = 3, k = 3
Output: "213"


Example 2:
Input: n = 4, k = 9
Output: "2314"

*/

public class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder result = new StringBuilder();

        List<Integer> numberList = new ArrayList<Integer>();
	for (int i=1; i<=n; i++) {
	    numberList.add(i);
	}

        int factorial_value = 1;
        for (int i=1; i<=n; i++) {
            factorial_value = factorial_value * i;
        }
 
        //modify k to be index
        k--;

        //calculate sequence
        for (int i=0; i<n; i++) {
            factorial_value = factorial_value / (n - i);
            int currentIndex = k / factorial_value;
            k = k % factorial_value;
 
            result.append(numberList.get(currentIndex));
            numberList.remove(currentIndex);
        }
 
        return result.toString();
    }
}
