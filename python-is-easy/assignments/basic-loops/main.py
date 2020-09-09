'''
Homework assignment for the 'Python is easy' course by Pirple.

Written by Ed Yablonsky.

It pprints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the
multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
It also adds "prime" to the output when the number is a prime
(divisible only by itself and one).
'''

for number in range(1, 101):
    output = "" # collects output for the number
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(number)
    isPrime = True # assume the number is a prime by default
    for divisor in range(2, number):
        if number % divisor == 0:
            isPrime = False #  mark the number as not a prime
    if isPrime:
        output += " prime"
    print(output)
