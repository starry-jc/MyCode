import java.util.Scanner;

public class Inches2Centimeters {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        final double cmInInch = 2.54;

        // Inputs:
        System.out.print("Enter inches: ");
        int inches = kb.nextInt();

        // Conversion:
        double cm = inches * cmInInch;

        //Output:
        System.out.println(inches + " inches = " + cm + " centimeters");
    }
}
