/*

Title:  Longest Duplicate Substring

Given a string S, consider all duplicated substrings: (contiguous)
substrings of S that occur 2 or more times.  (The occurrences may
overlap.)

Return any duplicated substring that has the longest possible
length.  (If S does not have a duplicated substring, the answer is "".)


Example 1:
Input: "banana"
Output: "ana"


Example 2:
Input: "abcd"
Output: ""

Note:
1) 2 <= S.length <= 10^5
2) S consists of lowercase English letters.

 */

class Solution {
    public String longestDupSubstring(String S) {
        int size = S.length();
        int[] nums = new int[size];
        for (int i=0; i<size; ++i) {
            nums[i] = (int)S.charAt(i) - (int)'a';        
        } 
        
        int a = 26;
        long modulus = (long)Math.pow(2, 32);

        int left = 1, right = size;
        int mid;
        while (left != right) {
            mid = left + (right - left) / 2;
            if (search(mid, a, modulus, size, nums) != -1) {
                left = mid + 1;                
            }
            else right = mid;
        }

        int start = search(left - 1, a, modulus, size, nums);
        if (start != -1) {
            return S.substring(start, start + left - 1);
        } else {
            return "";
        }
    }
    
    public int search(int mid, int a, long modulus, int size, int[] nums) {
        long hash = 0;
        for (int i=0; i<mid; ++i) {
            hash = (hash * a + nums[i]) % modulus;  
        } 

        HashSet<Long> visited = new HashSet();
        visited.add(hash);
        
        long aL = 1;
        for (int i=1; i<=mid; ++i) {
            aL = (aL * a) % modulus;  
        } 
        
        for (int start = 1; start < size - mid + 1; ++start) {
            hash = (hash * a - nums[start - 1] * aL % modulus + modulus) % modulus;
            hash = (hash + nums[start + mid - 1]) % modulus;
            if (visited.contains(hash)) {
                return start;
            }
            visited.add(hash);
        }
        return -1;
    }    
}
