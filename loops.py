# w use for loop to repeat an element from an iterable object

# for number in range(1, 10, 2):
#     print(f"number {number}")

# Give the corresponding numbers in  a giving string.
# add up those numbers

name = input("Your name: ").replace(" ", "")
add_corresp_number = 0
print("Here are the corresponding number of each letter in your name.")
for character in name:
    print(f"{character}: {ord(character)}")
    add_corresp_number += int(ord(character))
print(f"The total number is : {add_corresp_number}")


# exercise

# write a program that display all the even number from 1 to 10 and display the number of even number
count = 0
for numbers in range(1, 10):
    if numbers % 2 == 0:
        print(numbers)
        count += 1
print(f"We have {count} even numbers")
