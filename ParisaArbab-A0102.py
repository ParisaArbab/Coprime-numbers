"""
Author: Parisa Arbab
Date: Jan 17 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”


Questions:
• How efficient is coprime(a,b)? How did you ensure it was not making any needless computations?
• What assumptions does your code make? How easy is it for the user to crash your code?
"""

# Import math library to use the gcd function
import math


# Function to check if two numbers are coprime
def coprime(a, b):
    return math.gcd(a, b) == 1


# Function to repeatedly ask the user for two numbers and check if they are coprime
def coprime_test_loop():
    while True:
        # Ask the user for two numbers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Check if the numbers are coprime and print the result
        if coprime(num1, num2):
            print(f"{num1} and {num2} are coprime.")
        else:
            print(f"{num1} and {num2} are not coprime.")

        # Ask the user if they want to continue
        choice = input(
            "Do you want to check another pair of numbers? (yes/no): ").lower()  # convert user answer to lowercase
        if choice != "yes":
            break


# Main function to run the coprime test loop
if __name__ == "__main__":
    # Call the coprime test loop function
    coprime_test_loop()
