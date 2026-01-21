import config
from validator import validate_employee_data


def load_employees(filename=config.DATA_FILE):
    employees = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                    
                parts = line.split(config.DELIMITER)
                if len(parts) != len(config.EMPLOYEE_FIELDS):
                    print(f"Предупреждение: строка {line_num} пропущена - неверное количество полей")
                    continue
                
                employee = dict(zip(config.EMPLOYEE_FIELDS, parts))
                
                is_valid, message = validate_employee_data(employee)
                if not is_valid:
                    print(f"Предупреждение: строка {line_num} пропущена - {message}")
                    continue
                
                employee['salary'] = int(employee['salary'])
                employee['experience'] = int(employee['experience'])
                employee['birth_year'] = int(employee['birth_year'])
                employee['birth_month'] = int(employee['birth_month'])
                employee['birth_day'] = int(employee['birth_day'])
                
                employees.append(employee)
                
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return []
    except IOError as e:
        print(f"Ошибка при чтении файла: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return []
    
    return employees


def get_unique_departments(employees):
    departments = set()
    for emp in employees:
        departments.add(emp['department'])
    return sorted(list(departments))


def get_employee_count(employees):
    return len(employees)