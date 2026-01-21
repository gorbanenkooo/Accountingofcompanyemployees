import sys
import os
from data_handler import load_employees, get_unique_departments, get_employee_count
from sorter import sort_full_list, sort_by_department, sort_above_average_salary
from reporter import print_report, print_departments_list, print_statistics
from validator import validate_input_number, validate_department_name
import config


def display_menu():
    print("\n" + "="*60)
    print("ПРОГРАММА 'УЧЁТ СОТРУДНИКОВ'".center(60))
    print("="*60)
    print("1. Полный список сотрудников (сортировка: год рождения ↓, стаж ↓, фамилия ↑)")
    print("2. Список сотрудников отдела (сортировка: оклад ↓, фамилия ↑)")
    print("3. Сотрудники с окладом выше среднего (сортировка: должность ↑, фамилия ↑)")
    print("4. Показать статистику")
    print("5. Показать доступные отделы")
    print("6. Выход")
    print("="*60)
    
    while True:
        try:
            choice = input("Выберите пункт меню (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print("Ошибка! Введите число от 1 до 6.")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            sys.exit(0)


def handle_full_list(employees):
    if not employees:
        print("Нет данных о сотрудниках.")
        return
    
    print("\nФормирование полного списка сотрудников...")
    sorted_employees = sort_full_list(employees)
    print_report(sorted_employees, "ПОЛНЫЙ СПИСОК СОТРУДНИКОВ")
    
    input("\nНажмите Enter для продолжения...")


def handle_department_list(employees):
    if not employees:
        print("Нет данных о сотрудниках.")
        return
    
    departments = get_unique_departments(employees)
    
    if not departments:
        print("Нет данных об отделах.")
        return
    
    print_departments_list(departments)
    
    while True:
        department = input("\nВведите название отдела (или '0' для отмены): ").strip()
        
        if department == '0':
            return
        
        if validate_department_name(department, departments):
            break
        else:
            print("Ошибка! Такого отдела нет в списке. Попробуйте снова.")
    
    print(f"\nФормирование списка сотрудников отдела '{department}'...")
    sorted_dept_employees = sort_by_department(employees, department)
    
    if sorted_dept_employees:
        print_report(sorted_dept_employees, f"СОТРУДНИКИ ОТДЕЛА '{department.upper()}'")
    else:
        print(f"В отделе '{department}' нет сотрудников.")
    
    input("\nНажмите Enter для продолжения...")


def handle_above_average_salary(employees):
    if not employees:
        print("Нет данных о сотрудниках.")
        return
    
    print("\nРасчёт сотрудников с окладом выше среднего...")
    sorted_employees, avg_salary = sort_above_average_salary(employees)
    
    print(f"Средний оклад по предприятию: {avg_salary:,.2f} руб.")
    
    if sorted_employees:
        print_report(sorted_employees, "СОТРУДНИКИ С ОКЛАДОМ ВЫШЕ СРЕДНЕГО")
    else:
        print("Нет сотрудников с окладом выше среднего.")
    
    input("\nНажмите Enter для продолжения...")


def check_data_file():
    if not os.path.exists(config.DATA_FILE):
        print(f"Ошибка: файл с данными '{config.DATA_FILE}' не найден.")
        print("Создайте файл с данными или воспользуйтесь генератором тестовых данных.")
        return False
    
    try:
        with open(config.DATA_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if len(lines) < config.MIN_RECORDS:
            print(f"Предупреждение: в файле только {len(lines)} записей, требуется минимум {config.MIN_RECORDS}")
            print("Рекомендуется добавить больше данных.")
            response = input("Продолжить? (да/нет): ").lower()
            if response not in ['да', 'д', 'yes', 'y']:
                return False
    except Exception as e:
        print(f"Ошибка при проверке файла: {e}")
        return False
    
    return True


def main():
    print("Загрузка данных...")
    
    if not check_data_file():
        print("Программа завершена.")
        return
    
    employees = load_employees()
    
    if not employees:
        print("Не удалось загрузить данные о сотрудниках.")
        print("Проверьте файл employees.txt и попробуйте снова.")
        return
    
    print(f"Загружено {len(employees)} записей о сотрудниках.")
    
    if len(employees) < config.MIN_RECORDS:
        print(f"Предупреждение: загружено только {len(employees)} записей, требуется минимум {config.MIN_RECORDS}")
        response = input("Продолжить? (да/нет): ").lower()
        if response not in ['да', 'д', 'yes', 'y']:
            return
    
    while True:
        try:
            choice = display_menu()
            
            if choice == '1':
                handle_full_list(employees)
            elif choice == '2':
                handle_department_list(employees)
            elif choice == '3':
                handle_above_average_salary(employees)
            elif choice == '4':
                print_statistics(employees)
                input("\nНажмите Enter для продолжения...")
            elif choice == '5':
                departments = get_unique_departments(employees)
                print_departments_list(departments)
                input("\nНажмите Enter для продолжения...")
            elif choice == '6':
                print("\nСпасибо за использование программы!")
                break
        
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")
            print("Пожалуйста, сообщите об этом разработчику.")
            input("Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()