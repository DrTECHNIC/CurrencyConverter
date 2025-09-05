def main():
    currency = {
        "USD": 0.012,
        "EUR": 0.01,
        "RUB": 1,
        "IDR": 202.06,
        "KZT": 6.63,
        "GBR": 0.0091
    } # НА МОМЕНТ 13:45 05.09.2025
    cur1 = input("Введите название валюты: ")
    cur2 = input("Введите название валюты: ")
    val = float(input("Введите значение для конвертации: "))
    print(f"{val} {cur1} = {(val/currency[cur1]) * (currency[cur2])} {cur2}")

if __name__ == "__main__":
    main()