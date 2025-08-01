def main():
    recipe_book = {
        "Pancakes": ["flour", "milk", "eggs", "sugar"],
        "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
    }
    
    print(recipe_book["Pancakes"])
    
    recipe_book["Smoothie"] = ["banana", "milk", "honey"]
    
    # tmp = recipe_book["Smoothie"]
    # tmp.append("blueberries")
    # recipe_book["Smoothie"] = tmp
    recipe_book["Smoothie"].append("blueberries")
    
    print(recipe_book)


if __name__ == "__main__":
    main()