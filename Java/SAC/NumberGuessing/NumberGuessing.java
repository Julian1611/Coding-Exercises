public class NumberGuessing {
  public static void main(String[] args) {

    // for loop isn't working???
    int i = UserInput.getInteger("Guess the number from 1 to 100, you have 10 chances: ");
    int mystery = (int)(Math.random() *100) + 1;

    for (f = 0, f <= 10, f++)
    {
      if (i != mystery)
      {
        System.out.println("Sorry, wrong number...");
        i = UserInput.getInteger("Guess again, you have still " + 10-f " chances left!");
      }else{
        System.out.println("You guessed it, congrats! It was " + mystery);
        f =11;
        //break?
      }
    }
  }
}
