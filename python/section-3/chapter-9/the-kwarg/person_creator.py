def create_person(**kwargs):
    dict = kwargs
    print("Person created with properties:")
    for key, value in dict.items():
        print(f"{key}: {value}")
        