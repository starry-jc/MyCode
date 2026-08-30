import java.util.Scanner;

public class Circles {
    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);

        // Inputs:
        System.out.print("Enter the radius: ");
        double radius = kb.nextDouble();

        // Calculations:
        double circumference = 2 * radius * Math.PI;
        double area = radius * radius * Math.PI;

        // Outputs:
        System.out.println("Radius of the circle: " + radius);
        System.out.println("Circumference of the circle: " + circumference);
        System.out.println("Area of the circle: " + area);
    }
}
