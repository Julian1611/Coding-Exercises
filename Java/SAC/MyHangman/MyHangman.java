/**
 * @(#)MyHangman.java
 *
 *This game uses the hangman game engine to handle all the sound and pictures,
 *the GUI. (Graphical User Interface) SO MUST HAVE HangMan.class IN PROJECT FOLDER!
 *
 *First a user is asked to enter a phrase and then a second user
 *is given a chance to guess the letters in the phrase. Each time a correct
 *letter is guessed the second user is asked to guess what the phrase might
 *be. But if the second user chose a letter not in the phrase then a picture is
 *displayed. When six incorrect letters are guessed the game is over, or
 *when the second user correctly guesses the phrase the game is over.
 *
 *The hangman game engine has the following useful methods:
 *setPhrase(String phrase, int amountOfLetters)
 *the phrase must have lowercase letters and optional spaces and/or the
 *following puncutation ';:.,?!
 *the amountOfLetters must equal the amount of lowercase letters only, it
 *must not include spaces or punctation or the engine won't work.
 *
 *guessedLetterWrong(String guessedLetter, int amountOfWrongGuesses)
 *guessedLetter is whatever the user entered as their current guess
 *amountOfWrongGuesses is a count of how many wrong guesses the user has made
 *to this point
 *
 *guessedLetterRight(String guessedLetter, int position)
 *guessedLetter is whatever the user entered as their current guess
 *position is the location of that letter within the phrase, this may need to
 *be in a loop if the same letter appears more than once in the phrase
 *
 *guessedPhraseRight() and guessedPhraseWrong()
 *these are used when the second user correctly chooses a letter and then
 *makes a guess at what the phrase is. If the guess is correct then
 *use guessedPhraseRight() otherwise use guessedPhraseWrong()
 *
 * @author Taylor Swift
 * @version 1.00 2016/01/5
 */
import javax.swing.*;

public class MyHangman
{
  public static void main(String[] args)
  {
  	int count = 0;
  	int pos;
  	int countChar = 0;
  	String choice;
  	String words;
  	String guess;

    // TODO code application logic here
    // Sample test case for HangMan game engine
    // Requires the HangMan class...where to find?
    HangMan hm = new HangMan("My super cool game!");

    String phrase= JOptionPane.showInputDialog("Type a phrase: ");
    hm.setPhrase(phrase, phrase.length);
    //have a loop that goes until the user guesses the phrase
    //should maybe also stop when six incorrect guesses are made
  	while (true)
  	{
  		while ((choice = JOptionPane.showInputDialog("Guess a letter: ")).length() != 1);
    	char charGuessed = choice.charAt(0);

    	//check if the letter is in the phrase
    	if(phrase.indexOf(charGuessed) >= 0)
    	{
    		//got the letter right so find out where all it appears and use
  			// guessedLetterRight as many times as needed
  			pos = phrase.indexOf(charGuessed);

  			while(pos != -1)
  			{
  				countChar++;
  				hm.guessedLetterRight(choice, pos);
  				pos = phrase.indexOf(charGuessed, pos+1);
  			}
  			//get the user's guess and either use hm.guessedPhraseRight() or
  			//use hm.guessedPhraseWrong() depending if the guess was right or not

  			guess = JOptionPane.showInputDialog("Guess the phrase: ");
  			if (guess.equals(phrase))
  			{
  				hm.guessedPhraseRight();
  				System.out.println("correct guess");
  			}
  			else
  			{
  				hm.guessedPhraseWrong();
  				System.out.println("wrong guess");
  			}
    	}
    	else
    	{
    		//keep a count of how many wrong guesses
    		count ++;
    		hm.guessedLetterWrong(choice, count);
    		System.out.println(count);
    		//if count == 6 --> Game Over
    	}
  	}
  }
}
