def print_employee(emp, index=None):
    if index is not None:
        print(f"{index:3}. ", end="")
    
    print(f"{emp['last_name']} {emp['first_name']} {emp['patronymic']}, "
          f"рожд. {emp['birth_day']:02d}.{emp['birth_month']:02d}.{emp['birth_year']}, "
          f"{emp['department']}, {emp['position']}, "
          f"оклад: {emp['salary']:,} руб., стаж: {emp['experience']} лет")


def print_report(employees, title):
    print(f"\n{'='*60}")
    print(f"{title:^60}")
    print(f"{'='*60}")
    
    if not employees:
        print("Нет данных для отображения")
        return
    
    for i, emp in enumerate(employees, 1):
        print_employee(emp, i)
    
    print(f"{'='*60}")
    print(f"Всего записей: {len(employees)}")


def print_departments_list(departments):
    print("\nДоступные отделы:")
    for i, dept in enumerate(departments, 1):
        print(f"{i:2}. {dept}")


def print_statistics(employees):
    if not employees:
        print("Нет данных для статистики")
        return
    
    total_salary = sum(emp['salary'] for emp in employees)
    avg_salary = total_salary / len(employees)
    max_salary = max(emp['salary'] for emp in employees)
    min_salary = min(emp['salary'] for emp in employees)
    
    departments = {}
    for emp in employees:
        dept = emp['department']
        departments[dept] = departments.get(dept, 0) + 1
    
    print("\nСтатистика по сотрудникам:")
    print(f"Всего сотрудников: {len(employees)}")
    print(f"Средний оклад: {avg_salary:,.2f} руб.")
    print(f"Максимальный оклад: {max_salary:,} руб.")
    print(f"Минимальный оклад: {min_salary:,} руб.")
    print("\nКоличество сотрудников по отделам:")
    for dept, count in sorted(departments.items()):
        print(f"  {dept}: {count} чел.")