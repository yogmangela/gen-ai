#Task 1: Print Multiplication Table
#Write a program that takes an integer n as input and prints the multiplication table for n (from 1
#to 10) using a for loop.

from colorama import Fore, Style, init
import time

init(autoreset=True)

n = int(input(Fore.CYAN + "Enter a number: "))

print(Fore.YELLOW + f"\nMultiplication Table for {n}:\n" + "-" * 30)
for i in range(1, 11):
    print(Fore.GREEN + f"{n} × {i} = {n * i}")
    time.sleep(0.3)  # Adds a smooth animation effect