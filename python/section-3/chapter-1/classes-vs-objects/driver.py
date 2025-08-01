from student import Student


def main():
    s1 = Student("Alice", "A")
    s2 = Student("Bob", "B")
    
    print(f"{s1.name} has grade {s1.grade} at {Student.school}")
    print(f"{s2.name} has grade {s2.grade} at {Student.school}")

if __name__ == "__main__":
    main()