from temperature import run_temperature_converter
from currency import run_currency_converter
from length import run_length_converter
from time_duration import run_time_duration_converter
from volume import run_volume_converter
from number_bases import run_number_bases_converter

def main():
    while True:
        print()
        print("UNIT CONVERTER\n1 - Temperature Converter\n2 - Currency Converter\n3 - Length Converter\n4 - Time and Duration Converter\n5 - Volume Converter\n6 - Number Bases Converter\n7 - Exit")
        try:
            option = int(input("Choose an option - "))
        except ValueError:
            print("Invalid option. Please, enter a number from 1 to 7.")
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
            run_volume_converter()
        elif option == 6:
            run_number_bases_converter()
        elif option == 7:
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()