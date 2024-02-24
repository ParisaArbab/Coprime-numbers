# Coprime-numbers
use gcd (Greatest Common Divisor) function from math library for determining if two numbers are coprime.
This code defines a Python program to determine if two numbers are coprime, meaning they have no common divisors other than 1. Here's a summary of its components and how it works:

Import Math Library: The program starts by importing the math library to use its gcd (Greatest Common Divisor) function, essential for determining if two numbers are coprime.

Coprime Function: It defines a function named coprime(a, b) which takes two numbers as input and returns True if their greatest common divisor is 1, indicating they are coprime. Otherwise, it returns False.

Coprime Test Loop Function: This function, coprime_test_loop(), creates an interactive loop where the user is repeatedly asked to input two numbers. For each pair of numbers, the program checks if they are coprime using the coprime function and prints the result. After each check, the user is asked if they want to test another pair of numbers. If the user answers anything other than "yes," the loop breaks, and the program ends.

Main Execution: In the main execution block (if __name__ == "__main__":), the program calls the coprime_test_loop function to start the interactive loop. This allows users to continuously input pairs of numbers to find out if they are coprime until they decide to stop.
