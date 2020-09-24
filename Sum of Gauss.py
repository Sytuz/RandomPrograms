import time
import sys

print("""
----------------------------------------------
This  program  takes  two   numbers  and  adds
all  the  numbers  in  between them, including
themselves.
----------------------------------------------
""")

time.sleep(3)

statement = True

while statement:
    try:
        number_1 = int(input("\nInsert the first number.\n"))
        if number_1:
            number_2 = int(input("\nInsert the second number.\n"))
    except ValueError:
        print("That's not a number!")
        time.sleep(1)
        for i in range(3):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            sys.stdout.flush()
        continue
    total_sum = 0
    if number_1 > number_2:
        for number in range(number_2, number_1+1):
            total_sum += number
        statement = False
    elif number_1 < number_2:
        for number in range(number_1, number_2+1):
            total_sum += number
        statement = False
    elif number_1 == number_2:
        total_sum = number_1 + number_2
        statement = False
    else:
        continue
    print("The total sum is {}!".format(total_sum))