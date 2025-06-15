from temperature import run_temperature_converter
from currency import run_currency_converter
from length import run_length_converter
from time_duration import run_time_duration_converter

def main():
    while True:
        print()
        print("UNIT CONVERTER\n1 - Temperature Converter\n2 - Currency Converter\n3 - Length Converter\n4 - Time and Duration Converter\n5 - Exit")
        try:
            option = int(input("Choose an option - "))
        except ValueError:
            print("Invalid option. Please, enter a number from 1 to 5.")
            return
        print()
        if option == 1:
            run_temperature_converter()
        elif option == 2:
            run_currency_converter()
        elif option == 3:
            run_length_converter()
        elif option == 4:
            run_time_duration_converter()
        elif option == 5:
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()