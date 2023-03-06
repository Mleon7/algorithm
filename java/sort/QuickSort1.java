package sort;

import java.util.Arrays;

import static sort.Utils.swap;

public class QuickSort1 {
    public static void main(String[] args) {
        int[] a = {5, 3, 7, 2, 9, 8, 1, 4};
        quick_sort(a, 0, a.length - 1);
    }

    public static void quick_sort(int[] a, int l, int h) {
        if(l >= h) {
            return;
        }
        int p = partition(a, l, h); // p 索引值
        quick_sort(a, l, p-1); // 左边分区的范围确定
        quick_sort(a, p+1, h); // 右边分区的范围确定
    }

    private static int partition(int[] a, int l, int h) {
        int pv = a[h]; // 基准点元素
        int i = l;
        for (int j = l; j < h; j++) {
            if(a[j] < pv) {
                // 为了优化，可不加if
                if(i != j) {
                    swap(a, i, j);
                }
                i++;
            }
        }
        // 为了优化，可不加if
        if(i != h) {
            swap(a, h, i);
        }
        System.out.println(Arrays.toString(a) + " i=" + i);

        // 返回值代表了基准点元素所在的正确索引，用它确定下一轮分区的边界
        return i;
    }
}
