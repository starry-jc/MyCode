public class Receipt3 {
    public static void main(String [] args)
   {
      // Receipt 2 variables
      String highSchool = "ECHHS";
      double drinkPrice = 1.50;
      double candyPrice = 1.25;
      double hotDogPrice = 2.75;
      double hamburgerPrice = 3.50;

      // Receipt 3 variables
      int orderNum = 5;
      int numDrinks = 7;
      int numCandies = 45;
      int numHotDogs = 65;
      int numHamburgers = 62;
      double taxRate = 0.08;
      double subtotal = drinkPrice*numDrinks + candyPrice*numCandies + hotDogPrice*numHotDogs + hamburgerPrice*numHamburgers;
      double total = subtotal + taxRate*subtotal;

      // Receipt 1 Output (w/ receipt 2 concatenation)
      System.out.println("**************************************");
      System.out.println("*                                    *");
      System.out.println("*          "+highSchool+" Snack Bar           *");
      System.out.println("*                                    *");
      System.out.println("*     Drink ..........$"+drinkPrice+0+"          *");                      
      System.out.println("*     Candy ..........$"+candyPrice+"          *");     
      System.out.println("*     Hot Dog ........$"+hotDogPrice+"          *");     
      System.out.println("*     Hamburger ......$"+hamburgerPrice+0+"          *");     
      System.out.println("*                                    *");    
      System.out.println("**************************************");

      // Receipt 3
      System.out.println("*     Order Number  "+orderNum+"                *");
      System.out.println("*                                    *");
      System.out.println("*     QTY      ITEM      TOTAL       *");
      System.out.println("**************************************");
      System.out.println("*      "+numDrinks+"       Drink     "+(numDrinks*drinkPrice)+0+"       *");
      System.out.println("*      "+numCandies+"      Candy     "+(numCandies*candyPrice)+"       *");
      System.out.println("*      "+numHotDogs+"     Hot Dog    "+(numHotDogs*hotDogPrice)+"      *");
      System.out.println("*      "+numHamburgers+"    Hamburger   "+(numHamburgers*hamburgerPrice)+0+"      *");
      System.out.println("**************************************");
      System.out.println("*     Subtotal      "+subtotal+"            *");
      System.out.println("*     Tax           "+taxRate*subtotal+0+"            *");
      System.out.println("*     Total        "+total+0+"            *");
   }
}
