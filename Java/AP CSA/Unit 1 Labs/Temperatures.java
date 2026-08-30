import java.util.Scanner;

public class Temperatures {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        // Inputs:
        System.out.print("Enter a temperature in degrees Fahrenheit: ");
        double fahrenheit_temp = kb.nextInt();
        
        // Calculations:
        double celcius_temp = (5 * (fahrenheit_temp - 32)) / 9;

        // Output:
        System.out.printf("%.1f F = %f C\n", fahrenheit_temp, celcius_temp);
    }
}
