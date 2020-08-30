//Pancake sorting

class Solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> list = new ArrayList();
        for (int n = A.length; n > 0; n--) {
            int index = find(A, n);
            flip(A, index);
            flip(A, n - 1);
            list.add(index + 1);
            list.add(n);
        }

        return list;
    }
    
    private int find(int[] A, int target) {
        for (int i=0; i<A.length; i++) {
            if (A[i] == target) {
                return i;
            }
        }
        return -1;
    }

    private void flip(int[] A, int j) {
        int i = 0;
        while (i < j) {
            int temp = A[i];
            A[i++] = A[j];
            A[j--] =  temp;
        } 
    }
}
