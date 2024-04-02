# problem 2, Make a factorial calculator
num = int(input("Enter an integer and I will calculate its factorial number: "))
multiplier = num #set multiplier to input. will later change to the result of the multiplication
# account for special cases
if num == 0:
    print("0! = 1")
elif num < 0:
    print("Factorials of negative numbers do not exist")
elif num == 1:
    print("1! = 1")
else:
    num_list = []
    for item in range((num-1), 0, -1): #count down
        #print(f"Item {item}, Multiplier {multiplier}")
        multiplier = multiplier * item
        num_list.append(str(item)) #append as string so i can join them
    print(f"{num}! = {num} * {' * '.join(num_list)} = {multiplier}")
#goofy ahh code