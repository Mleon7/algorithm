public class BinarySearch {
    public static void main(String[] args) {
        int[] array = {1, 5, 8, 11, 19, 22, 31, 35, 40, 45, 48, 49, 50};
        int target = 47;
        int idx = binarySearch(array, target);
        System.out.println(idx);
    }

    // 二分查找，找到返回元素索引，找不到返回 -1
    public static int binarySearch(int[] a, int t) {
        // 定义左边界L，右边界R
        int l = 0, r = a.length - 1, m;
        while(l <= r) {
            // 获取中间索引的值 M = Floor((L + R) / 2)
            m = (l + r) / 2;

            // 中间索引的值 A[M]与待搜索的值T进行比较
            // （1）A[M]==T 表示找到，返回中间索引
            if(a[m] == t) {
                return m;
            } else if(a[m] > t) {   // （2）A[M]>T，中间值右侧的其它元素都大于T，无需比较，中间索引左边去找，M-1设置为右边界，重新查找
                r = m - 1;
            } else {
                l = m + 1; // （3）A[M]<T，中间值左侧的其它元素都小于T，无需比较，中间索引左边去找，M+1设置为左边界，重新查找 
            }
        }

        return -1;
    }
}
