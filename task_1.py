def say_hello_if_more_then_7(number: int) -> str:
    if number > 7:
        return "Привет"


if __name__ == '__main__':
    number_to_check = input("Please, enter a number: ")
    if number_to_check.isdigit():
        print(say_hello_if_more_then_7(int(number_to_check)))
    else:
        print("Nice try, but numbers only")