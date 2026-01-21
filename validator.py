def validate_employee_data(employee):
    for field in ['last_name', 'first_name', 'department', 'position']:
        if not employee.get(field) or not isinstance(employee[field], str):
            return False, f"Неверное значение поля {field}"
    
    try:
        birth_year = int(employee['birth_year'])
        if not (1900 <= birth_year <= 2005):
            return False, f"Некорректный год рождения: {birth_year}"
        
        birth_month = int(employee['birth_month'])
        if not (1 <= birth_month <= 12):
            return False, f"Некорректный месяц рождения: {birth_month}"
        
        birth_day = int(employee['birth_day'])
        if not (1 <= birth_day <= 31):
            return False, f"Некорректный день рождения: {birth_day}"
        
        salary = int(employee['salary'])
        if salary <= 0:
            return False, f"Некорректный оклад: {salary}"
        
        experience = int(employee['experience'])
        if experience < 0:
            return False, f"Некорректный стаж: {experience}"
            
    except (ValueError, KeyError):
        return False, "Ошибка при преобразовании числовых полей"
    
    return True, "Данные корректны"


def validate_input_number(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = input(prompt)
            num = int(value)
            
            if min_val is not None and num < min_val:
                print(f"Значение должно быть не меньше {min_val}")
                continue
                
            if max_val is not None and num > max_val:
                print(f"Значение должно быть не больше {max_val}")
                continue
                
            return num
            
        except ValueError:
            print("Ошибка! Введите целое число.")


def validate_department_name(department, available_departments):
    return department in available_departments