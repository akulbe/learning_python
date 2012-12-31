__author__ = 'Aaron Kulbe'
# convert.py
#   A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
#
# Note: this isn't a copy & paste. I'm typing it in exactly as I found it in the John Zelle book.

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()