
menu = [
    {"name": "Піца", "price": 250, "description": "З шинкою та грибами", "category": "Main"},
    {"name": "Сік", "price": 45, "description": "Апельсиновий", "category": "Drinks"}
]


def add_dish():

    pass


def edit_dish():

    pass



def delete_dish():
    print("\n--- МЕНЮ ВИДАЛЕННЯ (Учасник В) ---")
    print("1. Видалити страву за назвою")
    print("2. Видалити всі страви за категорією")
    print("3. Скасувати")

    sub_choice = input("Оберіть дію: ")

    if sub_choice == "1":
        name_to_delete = input("Введіть назву страви для видалення: ").strip()
        initial_len = len(menu)

        menu[:] = [dish for dish in menu if dish['name'].lower() != name_to_delete.lower()]

        if len(menu) < initial_len:
            print(f" Страва '{name_to_delete}' видалена.")
        else:
            print(f" Страву '{name_to_delete}' не знайдено.")

    elif sub_choice == "2":
        cat_to_delete = input("Введіть категорію для видалення всіх її страв: ").strip()
        initial_len = len(menu)
        # Видаляємо всі страви вказаної категорії
        menu[:] = [dish for dish in menu if dish.get('category', '').lower() != cat_to_delete.lower()]

        deleted_count = initial_len - len(menu)
        if deleted_count > 0:
            print(f" Видалено страв у категорії '{cat_to_delete}': {deleted_count} шт.")
        else:
            print(f" В категорії '{cat_to_delete}' страв не знайдено.")

    # Підрахунок кількості страв (обов'язкова умова завдання В)
    print(f"📊 Поточна кількість страв у меню: {len(menu)}")




def show_menu():

    pass


def calculate_total():

    pass


def main():
    while True:
        print("\n--- RESTAURANT MENU ---")
        print("1. Додати страву (А)")
        print("2. Редагувати страву (Б)")
        print("3. Видалити страву (В - Твоя черга)")
        print("4. Показати меню (А)")
        print("5. Загальна ціна (Г)")
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
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()