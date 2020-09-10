package eyablonsky.pirple.java.ControlFlow;

/*
Homework assignment for the 'Fundamentals of Java' course by Pirple.

Written by Ed Yablonsky.

It pprints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the
multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
It also adds "prime" to the output when the number is a prime
(divisible only by itself and one).
*/

public class Program {
    public static void main(final String[] args) {
        for (int number = 1; number <= 100; number++) {
            String output = ""; // collects output for the number
            if (number % 3 == 0) {
                output = "Fizz";
            }
            if (number % 5 == 0) {
                output += "Buzz";
            }
            if (output.equals("")) {
                output = Integer.toString(number);
            }
            boolean isPrime = true; // assume the number is a prime by default
            for (int divisor = 2; divisor <  number; divisor++) {
                if (number % divisor == 0) {
                    isPrime = false; // mark the number as not a prime
                }
            }
            if (isPrime) {
                output += " prime";
                break;
            }
            System.out.println(output);
        }
    }
}
