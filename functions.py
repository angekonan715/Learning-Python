def save_user(**user):
    return user


user_1 = save_user(id=1, name="kouadio", country="civ", skin="black")

print(user_1)

# create a function that stores a list of args in tuple


def store_list(*numbers):
    return numbers


print(store_list(1, 2, 4, 5, 7, "ange"))
