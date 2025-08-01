def calculate_discount(price, discount_percentage):
    discount = price * discount_percentage
    price = round(price - discount, 2)
    return price
    

def main():
    print(calculate_discount(100, 0.2))  # Output: 80.0
    
if __name__ == "__main__":
    main()