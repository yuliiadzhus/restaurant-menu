menu = [
    {"name": "Піца", "price": 250, "description": "З шинкою та грибами", "category": "Main"},
    {"name": "Сік", "price": 45, "description": "Апельсиновий", "category": "Drinks"}
]

def edit_dish():
    print("\n--- РЕДАГУВАННЯ СТРАВИ (Учасник Б) ---")
    name_to_edit = input("Введіть назву страви, яку хочете змінити: ").strip()
    
     
    found_dish = None
    for dish in menu:
        if dish[' Піца '].lower() == name_to_edit.lower():
            found_dish = dish
            break
    
    if not found_dish:
        print(f" Страви з назвою '{name_to_edit}' не знайдено.")
        return

    print(f"Знайдено: {found_dish['name']} | Ціна: {found_dish['price']} | Опис: {found_dish['description']} | Категорія: {found_dish['category']}")
    
    
    new_price_str = input("Введіть нову ціну (залиште порожнім, щоб не змінювати): ").strip()
    if new_price_str:
        try:
            new_price = float(new_price_str)
           
            if new_price < 0:
                print("Помилка: ціна не може бути від'ємною.")
            else:
                found_dish['price'] = new_price
        except ValueError:
            print("Помилка: введіть число для ціни.")

    new_desc = input("Введіть новий опис (залиште порожнім, щоб не змінювати): ").strip()
    if new_desc:
        found_dish['description'] = new_desc

    new_cat = input("Введіть нову категорію (залиште порожнім, щоб не змінювати): ").strip()
    if new_cat:
        found_dish['category'] = new_cat
        
    print(f" Страву '{found_dish['name']}' успішно оновлено!")

    