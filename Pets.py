import os

def get_cats_info(path):
    try:
        #відкриває фаіл для його прочитання
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("Файл має бути не пустим")
            
            cats_info = []
            for line in lines:
                #розбиває речення по комам та присвоє перемінним значення.
                cat_id, name, age = line.strip().split(',')
                #створює словник по кожному окремому коту
                cat_dict = {"id": cat_id, "name": name, "age": age}
                #додає кота до списку
                cats_info.append(cat_dict)

            return cats_info

    except FileNotFoundError:
        print(f"Помилка: файл {path} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
