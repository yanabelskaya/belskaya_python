def say_hello_to_vyacheslav(user_name: str) -> str:
    return "Привет, Вячеслав" if user_name.lower() == "вячеслав" else "Нет такого имени"


if __name__ == '__main__':
    print(say_hello_to_vyacheslav(input("Молви, друг, и войди!: ")))
