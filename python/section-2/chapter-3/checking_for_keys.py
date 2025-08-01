def main():
    employees = {
        "Alice": "HR",
        "Bob": "Engineering",
        "Diana": "Marketing"
    }
    
    if "Alice" in employees.keys():
        print("Alice is in the company.")
    
    if "John" not in employees.keys():
        print("John is not in the company.")


if __name__ == "__main__":
    main()