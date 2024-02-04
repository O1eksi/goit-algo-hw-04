import os



def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("Файл має бути не пустим")
            
            total_sum = 0
            for line in lines:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_sum += salary

            total_count = len(lines)
            average_salary = total_sum / total_count

            return total_sum, average_salary

    except FileNotFoundError:
        print(f"Помилка: файл {path} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

# Приклад використання функції:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")