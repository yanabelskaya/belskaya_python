def print_elements_multiples_of_three(elements_list: list) -> list:
    return [i for i in elements_list if i % 3 == 0]


def get_number_from_user() -> list:
    list_to_check = []
    while True:
        user_input = input("Enter a number, enter 'q' to exit: ")
        if user_input == "q":
            break
        try:
            list_to_check.append(int(user_input))
        except ValueError:
            print("It is not a number, try again!")
    return list_to_check


if __name__ == "__main__":
    print(print_elements_multiples_of_three(list(get_number_from_user())))
