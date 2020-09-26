import time
import sys

print("""
----------------------------------------------
This  program  takes  two   numbers  and  adds
all  the  numbers  in  between them, including
themselves.
It's called the Gaussian Sum Problem.
----------------------------------------------
""")

time.sleep(3)

while True:
    while True:
        try:
            number_1 = int(input("\nInsert the first number.\n"))
            if number_1:
                number_2 = int(input("\nInsert the second number.\n"))
        except ValueError:
            print("That's not a number!")
            time.sleep(1)
            for i in range(4):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.flush()
            continue

        total_sum = 0
        numbers = 0
        big_number = 0
        small_number = 0

        if number_1 > number_2:
            for number in range(number_2, number_1+1):
                total_sum += number
            big_number = number_1
            small_number = number_2
            numbers = number_1 + 1 - number_2
            break
        elif number_1 < number_2:
            for number in range(number_1, number_2+1):
                total_sum += number
            big_number = number_2
            small_number = number_1
            numbers = number_2 + 1 - number_1
            break
        elif number_1 == number_2:
            total_sum = number_1 + number_2
            break
        else:
            continue

    if numbers % 2 == 0 and numbers != 0:
        count = int(numbers / 2)
        if count < 0:
            count = count * -1
        added = number_1 + number_2

        print(f"""
-----------------------------------------------------------------------------------------------------------
To solve the Gaussian Sum Problem applied to these numbers, {small_number} and {big_number}, we  first
need to visualize a list of all the numbers that exist in between these numbers, including themselves.
Now, we need to pair the first number with the last one, and add them together.
We can do this more than once to be sure, but the result is always the same: {added}.
Now, think about the amount of pairs that we have. If the number is even, we just need to divide the total
ammount of numbers by 2, which will give us {count}.
Finally, all we have to do is multiply the number of pairs, {count}, with the result we got from adding
them together, {added}, which will give us the final solution: {total_sum}.
-----------------------------------------------------------------------------------------------------------
        """)
    else:
        count = int(numbers / 2)
        if count < 0:
            count = count * -1
        middle = count + 1
        added = number_1 + number_2

        print(f"""
------------------------------------------------------------------------------------------------------------
To solve the Gaussian Sum Problem applied to these numbers, {small_number} and {big_number}, we first
need to visualize a list of all the numbers that exist in between these numbers, including themselves.
Now, we need to pair the first number with the last one, and add them together.
We can do this more than once to be sure, but the result is always the same: {added}.
As you notice, the result is always the same: {added}.
Now, think about the amount of pairs that we have. If the number is odd, then we need to divide the total
ammount of numbers by 2, and round down the result, which will give us {count}.
Finally, we have to multiply the number of pairs, {count} with the result we got from adding them together,
{added}, and add the remaining number, {middle}, giving us the final result: {total_sum}.
------------------------------------------------------------------------------------------------------------
    """)

    time.sleep(10)
    loop_out = 0  

    while True:
        answer = input("\nDo you want to try another pair of numbers? (yes/no)\n").lower().strip()
        if answer == "yes":
            break
        elif answer == "no":
            print("\nGoodbye!\n")
            time.sleep(1)
            loop_out += 1
            break
        else:
            print("\nPlease answer with a yes or a no.\n")
            time.sleep(1)
            for i in range(6):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                sys.stdout.flush()
    
    if loop_out == 1:
        break
    