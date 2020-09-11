package eyablonsky.pirple.java.Functions;

/*
Homework assignment for the 'Fundamentals of Java' course by Pirple.

Written by Ed Yablonsky.

It defines three functions according to the assignment and tests them.
*/

public class Program {
    /*
     * Accepts a string, constructs reversed version of it and returns.
     */
    public static String reverseString(String input) {
        String reversed = "";
        // Iterate over the input backwards
        for (int index = input.length() - 1; index >= 0; index--) {
            reversed += input.charAt(index);
        }
        return reversed;
    }

    /*
     * Returns True if the input string is a palindrome, means that it reads
     * the same from left to right and from right to left.
     * Otherwise returns False.
     * It ignores whitespaces and other non letter or non digit symbols.
     * It's also case insensitive.
     */
    public static boolean isPalindrome(String input) {
        int leftIndex = 0; // points to left character
        int rightIndex = input.length() - 1; // points to right character
        // Loop until the left and the right pointers met
        while (leftIndex < rightIndex) {
            char leftChar = Character.toLowerCase(input.charAt(leftIndex));
            char rightChar = Character.toLowerCase(input.charAt(rightIndex));
            if (Character.isLetterOrDigit(leftChar) == false) {
                // Move only left pointer towards
                leftIndex++;
                continue;
            }
            if (Character.isLetterOrDigit(rightChar) == false) {
                // Move only right pointer backwards
                rightIndex--;
                continue;
            }
            if (leftChar != rightChar) {
                // We found difference in characters,
                // so the input is not a palindrome
                return false;
            }
            // Move both pointers to new characters
            leftIndex++;
            rightIndex--;
        }
        // If we got to this point than the input is palindrome
        return true;
    }

    /*
     * Returns a random number between those min and max integers
     * (inclusive of them).
     */
    public static int randBetween(int min, int max) {
        int rangeSize = max - min;
        int rangeFraction = (int)Math.round(Math.random() * rangeSize);
        return min + rangeFraction;
    }

    public static void main(final String[] args) {
        boolean testsPassed = true;

        // Test reverseString
        testsPassed = testsPassed &&
            reverseString("").equals("") &&
            reverseString(" ").equals(" ") &&
            reverseString("one two three").equals("eerht owt eno");

        // Test isPalindrome
        testsPassed = testsPassed &&
            isPalindrome("") &&
            isPalindrome(" ") &&
            isPalindrome("  ") &&
            isPalindrome("noon") &&
            isPalindrome("moon") == false &&
            isPalindrome("mom") &&
            isPalindrome("Mom") &&
            isPalindrome("sator arepo tenet opera rotas") &&
            isPalindrome("Step on no pets") &&
            isPalindrome("My gym") &&
            isPalindrome("Was it a cat I saw?") &&
            isPalindrome("Eva, can I see bees in a cave?");

        // Test randomBetween
        int min = 33;
        int max = 55;
        for (int i = 0; i < 100; i++) {
            int number = randBetween(min, max);
            testsPassed = testsPassed && (number >= min) && (number <= max);
        }

        // Exit with error when a test is failed
        if (testsPassed == false) {
            System.exit(1);
        }
    }
}
