__author__ = 'Aaron Kulbe'

# File Chapter1_ProgrammingExercises_3.py
# A simple program illustrating chaotic behavior.


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()