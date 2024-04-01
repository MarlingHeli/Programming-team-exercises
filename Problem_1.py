#problem 1: Create an odd or even calculator,
# prints the value odd or even if the input integer is odd or even
while True:
    num = int(input("Enter an integer and I will check if it is even or odd: "))
    if num%2 == 0:
        print(f"{num} is an even number!\n")
    else:
        print(f"{num} is an odd number!\n")