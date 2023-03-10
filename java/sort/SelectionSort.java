package sort;

import java.util.Arrays;

import static sort.Utils.swap;

public class SelectionSort {
    public static void main(String[] args) {
        int[] a = {5, 3, 7, 2, 1, 9, 8, 4};
        selection(a);
    }

    private static void selection(int[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            // i 代表每轮选择最小元素要交换到的目标索引
            int s = i; // 代表最小元素的索引值
            for (int j = s+1; j < a.length; j++) {
                if(a[s] > a[j]) {
                    s = j;
                }
            }
            if (s != i) {
                swap(a, s, i);
            }
            System.out.println(Arrays.toString(a));
        }
    }
}
