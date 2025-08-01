def update_employee_info(employee_dict, key, value):
    employee_dict[key] = value
    return employee_dict
    
    
def main():
    ed = {"a": "A", "b": "B"}
    ed = update_employee_info(ed, "a", "a")
    print(ed)


if __name__ == "__main__":
    main()