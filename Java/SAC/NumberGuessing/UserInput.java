import java.util.Scanner;
import javax.swing.JOptionPane;

/**
 * The UserInput class provides static methods to retrieve input from the user. There are methods for
 * getting Strings and numbers (doubles or ints) using the console or a JOptionPane dialog box.
 * 
 * @author S. Zucca 
 * @version 2016
 */

public final class UserInput
{
    /**
     * Default message for display in any string input method 
     */
    private static final String STRING_INPUT_MESSAGE = "Input a String: ";
    
    /**
     * Default message for display in any integer input method 
     */
    private static final String INT_INPUT_MESSAGE = "Input an integer: ";
    
    /**
     * Default message for display in any double input method 
     */
    private static final String DOUBLE_INPUT_MESSAGE = "Input a number: ";
    
    private UserInput(){
        // can not be instantiated
    }
    
    /***
     * Create a Scanner object and print a message to ensure the console is ready.
     */
    private static Scanner initScanner(String message){
        Scanner scanner = new Scanner(System.in);
        
        System.out.print(message + " ");    // don't expect the user to provide proper spacing
        return scanner;
    }
    
    /***
     * Return a string from the console displaying a custom prompt
     * 
     * @param   message     A prompt for the user
     */
    public static String getString( String message ){
        Scanner scanner = initScanner(message);
        String data = scanner.nextLine();
        return data;
    }
    
    /***
     * Return a string from the console displaying default prompt
     */
    public static String getString(){
        return getString(STRING_INPUT_MESSAGE);
    }
    
    /***
     * Return a string from a dialog box showing a custom prompt (and a standard icon)
     * 
     * @param   message     A prompt for the user
     */
    public static String getStringDialog(String message){
        return JOptionPane.showInputDialog(null, message );
    }
    
    /***
     * Return a string from a dialog box showing a default prompt and icon.
     */
    public static String getStringDialog(){
        return getStringDialog(STRING_INPUT_MESSAGE);
        
    }
    
    /***
     * Return an integer from the console with custom prompt.
     * 
     * @param message   The custom prompt
     */
    public static int getInteger(String message){
        Scanner scanner = initScanner(message);
        Integer n = null;
        
        while(n == null) {
            try {
                n = scanner.nextInt();
            } catch(Exception e) {
                System.out.print( "Unable to convert input to an integer. Try again. " );
                scanner.skip(".*"); // skip over all buffered input
            }
        }

        
        return (int) n;
    }
    
    /***
     * Return an integer from the console with default prompt.
     */
    public static int getInteger(  ){
        return getInteger(INT_INPUT_MESSAGE);
    }
    
    /***
     * Return an integer from a dialog box showing a default prompt (and a standard icon)
     */
    public static int getIntegerDialog(){
        return getIntegerDialog(INT_INPUT_MESSAGE);
    }
            
    /***
     * Return an integer from a dialog box showing a custom prompt (and a standard icon)
     * 
     * @param   message     A prompt for the user
     */
    public static int getIntegerDialog(String message){
        
        // get the input and see if it can be made into an integer
        Integer n = null;
        String error_msg = "Unable to convert input to an integer. Try again.\n\n" + message;
        
        while(n == null) {
            try {    
                String input = JOptionPane.showInputDialog(null, message );
                n = Integer.parseInt(input);
            } catch(Exception e) {
                message = error_msg;
            }
        }
        
        return (int)n;
    }
    
    /***
     * Return a double from the console with custom prompt.
     * 
     * @param message   The custom prompt
     */
    public static double getDouble(String message){
        Scanner scanner = initScanner(message);
        Double d = null;
        
        while(d == null) {
            try {
                d = scanner.nextDouble();
            } catch(Exception e) {
                System.out.print( "Unable to convert input to a double. Try again. " );
                scanner.skip(".*"); // skip over all buffered input
            }
        }

        
        return d;
    }
    
    /***
     * Return a double from the console with default prompt.
     */
    public static double getDouble(  ){
        return getDouble(DOUBLE_INPUT_MESSAGE);
    }
    
    /***
     * Return a double from a dialog box showing a custom prompt (and a standard icon)
     * 
     * @param   message     A prompt for the user
     */
    public static double getDoubleDialog(String message){
        
        // get the input and see if it can be made into an integer
        Double d = null;
        String error_msg = "Unable to convert input to a number. Try again.\n\n" + message;
        
        while(d == null) {
            try {    
                String input = JOptionPane.showInputDialog(null, message );
                d = Double.parseDouble(input);
            } catch(Exception e) {
                message = error_msg;
            }
        }
        
        return (double)d;
    }
    
    /***
     * Return a double from a dialog box showing the default prompt (and a standard icon)
     */
    public static double getDoubleDialog(){
        return getDoubleDialog(DOUBLE_INPUT_MESSAGE);
    }
        
}