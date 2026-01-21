def merge_sort(arr, key_func):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted = merge_sort(left_half, key_func)
    right_sorted = merge_sort(right_half, key_func)
    
    return merge(left_sorted, right_sorted, key_func)


def merge(left, right, key_func):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_key = key_func(left[i])
        right_key = key_func(right[j])
        
        if left_key <= right_key:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


def sort_full_list(employees):
    def key_func(emp):
        return (-emp['birth_year'], -emp['experience'], emp['last_name'].lower())
    
    return merge_sort(employees, key_func)


def sort_by_department(employees, department):
    def key_func(emp):
        return (-emp['salary'], emp['last_name'].lower())
    
    department_employees = [emp for emp in employees if emp['department'] == department]
    return merge_sort(department_employees, key_func)


def sort_above_average_salary(employees):
    if not employees:
        return []
    
    total_salary = sum(emp['salary'] for emp in employees)
    average_salary = total_salary / len(employees)
    
    def key_func(emp):
        return (emp['position'].lower(), emp['last_name'].lower())
    
    above_average = [emp for emp in employees if emp['salary'] > average_salary]
    return merge_sort(above_average, key_func), average_salary