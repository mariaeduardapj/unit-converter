from temperature import run_temperature_converter
from currency import run_currency_converter
from length import run_length_converter

def main():
    print("UNIT CONVERTER\n1 - Temperature Converter\n2 - Currency Converter\n3 - Length Converter")
    try:
        option = int(input("Choose an option - "))
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 2.")
        return

    if option == 1:
        run_temperature_converter()
    elif option == 2:
        run_currency_converter()
    elif option == 3:
        run_length_converter()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()