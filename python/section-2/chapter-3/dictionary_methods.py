def main():
    grades = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78
    }

    print("Students:", grades.keys())
    print("Grades:", grades.values())

    grades["Diana"] = 92

    print("Bob's grade:", grades.get("Bob"))

    grades.pop("Charlie")
    print("Updated grades:", grades)


if __name__ == "__main__":
    main()