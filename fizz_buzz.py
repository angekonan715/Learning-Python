def fizz_buzz(user_input):
    if (user_input % 3 == 0) and (user_input % 5 == 0):
        return "FizzBuzz"
    if user_input % 3 == 0:
        return "Fizz"
    if user_input % 5 == 0:
        return "Buzz"
    return user_input


print(fizz_buzz(15))
