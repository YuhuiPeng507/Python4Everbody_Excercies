# Exercise 6: Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes.

numbers = []
while True:
    num = input("Enter a number:")
    if num != "done":
        if num.isnumeric() == True:
            numbers.append(num)
        else:
            print("value entered is not numeric")
            continue

    elif num == "done":
        print("done")
        break

# num_max = max(numbers)
# num_min = min(numbers)

if len(numbers)>0:
    print("the max number entered is: ", max(numbers))
    print("the min number entered is: ", min(numbers))
else:
    print("no numeric numbers are entered")