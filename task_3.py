def print_elements_multiples_of_three(elements_list: list) -> list:
    return [i for i in elements_list if i % 3 == 0]


if __name__ == '__main__':
    list_to_check = map(int, input("Please, input some numbers by space and click enter: ").split(" "))
    print(print_elements_multiples_of_three(list(list_to_check)))
