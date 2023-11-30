# python is an open source, cross.
print("Hello world ")
print("I am glad to learn python")

# working on strings
my_course = "Python leaning"

print(len(my_course))

# escaping character

# add a backslash to our code this way: //
# add a new line : /n
# add a double quote : /""
# add a single quote : /'

print("My name is : \n Kouadio")
print('He said: \"I am happy to be a programmer"')


first_name = input("Your first name :")
last_name = input("Your last name : ")

# print(f"You first name is : {first_name.title()}")
# print(f"Your last name is {last_name.title()}")


# strings methods

print(first_name.find("Ange"))
print(last_name.upper())
print(last_name.lower())
print(last_name.title())
print(last_name.strip())
print(last_name.lstrip())
print(last_name.rstrip())


# if statements

age = 22
if age >= 18:
    print("eligible")
else:
    print("Not eligible")

print("different ways for the above statement")

message = "eligible" if age >= 18 else "not eligible"
print(message)
