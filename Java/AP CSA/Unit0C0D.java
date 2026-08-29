import java.util.Scanner;

public class Unit0C0D {
    public static void main(String[] args) {
        // Unit 0C: Input

        Scanner keyboard = new Scanner(System.in);

        // Problem: nextLine() method reads in the \n from pressing the enter key
        //  nextInt doesn't read the \n, so nextLine picks it up
        System.out.print("Enter an integer :: ");
        int num = keyboard.nextInt();
        
        System.out.print("Enter a sentence :: ");
        String sentence = keyboard.nextLine();
        System.out.println(num + "" + sentence);

        // Solution: adding a nextLine() method after the nextInt()
        System.out.print("Enter an integer :: ");
        num = keyboard.nextInt();
        keyboard.nextLine();
        
        System.out.print("Enter a sentence :: ");
        sentence = keyboard.nextLine();
        System.out.println(num + "" + sentence);

        // Multiple Values
        //  If multiple values are inputted into one line, the first few select
        //  values will output based on the number of nextInt() methods called
        System.out.println(keyboard.nextInt());
        System.out.println(keyboard.nextInt()); 
        System.out.println(keyboard.nextInt()); 

        // Unit 0D: Math Operations

        // Returns integer
        System.out.println(1/2);
        
        // Returns decimal
        System.out.println(1.0/2.0);

        // As long as there is 1 decimal, returns decimal
        System.out.println(1/2.0);
        System.out.println(1.0/2);

        // = += -= *= /= %= are all below PEMDAS
        num = 27;
        num *= 2;
        System.out.println(num);

        num /= 5;
        System.out.println(num);

        num = num + 4 / 2 - 8;
        System.out.println(num);

        num = (4 + 5)/2+7;
        System.out.println(num);
        
        // Casting allows temporary changing of a data type for a value
        int one = 11;
        int two = 5;
        double dec = (double)one/two;
        System.out.println(dec);
    }
}
