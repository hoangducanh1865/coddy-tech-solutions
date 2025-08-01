def create_student_dict(name, age, major):
    dict = {
        "name": name,
        "age": age,
        "major": major
    }
    return dict
    

def main():
    dict = create_student_dict("Alice", 20, "Computer")
    print(dict)
    

if __name__ == "__main__":
    main()