import java.util.Arrays;

public class shiva {
    public static void main(String[] args) {
        
        int[] arr = {5, 2, 9, 1, 3};

        int sum = 0;
        for(int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        System.out.println("Sum of array elements: " + sum);

        Arrays.sort(arr);

        System.out.println("Sorted array:");
        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
