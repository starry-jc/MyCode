import java.util.Scanner;

public class Casting {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        // Input:
        System.out.print("Enter a double value: ");
        double doubleVal = kb.nextDouble();

        // Output:
        int intVal = (int)doubleVal;
        System.out.printf("%f cast to an int is %d", doubleVal, intVal);
    }
}
