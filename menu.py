menu = [
    {"name": "Піца", "price": 250, "description": "З шинкою та грибами", "category": "Main"},
    {"name": "Сік", "price": 45, "description": "Апельсиновий", "category": "Drinks"}
]
def add_dish():
    pass
def edit_dish():
    pass
def delete_dish():
    pass
def show_menu():
    pass
def calculate_total():
    pass
def main():
    while True:
        print("\n--- RESTAURANT MENU ---")
        print("1. Додати страву")
        print("2. Редагувати страву")
        print("3. Видалити страву")
        print("4. Показати меню")
        print("5. Загальна ціна")
        print("0. Вихід")

        choice = input("Виберіть дію: ")
        if choice == "1":
            add_dish()
        elif choice == "2":
            edit_dish()
        elif choice == "3":
            delete_dish()
        elif choice == "4":
            show_menu()
        elif choice == "5":
            calculate_total()
        elif choice == "0":
            break

if __name__ == "__main__":
    main()