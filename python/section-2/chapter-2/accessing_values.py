def get_capital(country_capitals, country_name):
    capital_name = country_capitals[country_name]
    return capital_name
    

def main():
    country_capitals = {"Norway": "Oslo", "Sweden": "Stockholm", "Denmark": "Copenhagen"}
    print(get_capital(country_capitals, "Norway"))


if __name__ == "__main__":
    main()