import java.util.Scanner;

public class Averages {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        // Input Section
        System.out.print("Enter your 1st integer: ");
        int integer1 = keyboard.nextInt();

        System.out.print("Enter your 2nd integer: ");
        int integer2 = keyboard.nextInt();

        System.out.print("Enter your 3rd integer: ");
        int integer3 = keyboard.nextInt();

        // Calculations
        double average = (double)(integer1 + integer2 + integer3) / 3;

        // Output
        System.out.printf("Your integers were the following: %d, %d, %d\n", integer1, integer2, integer3);
        System.out.println("Your average is: " + average);
    }

}
