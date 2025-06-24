from temperature import run_temperature_converter
from currency import run_currency_converter
from length import run_length_converter
from time_duration import run_time_duration_converter
from volume import run_volume_converter
from number_bases import run_number_bases_converter
from digital_storage import run_digital_storage_converter
from weight import run_weight_converter
from area import run_area_converter
from energy import run_energy_converter
from pressure import run_pressure_converter

def main():
    while True:
        print()
        print("UNIT CONVERTER\n01 - Temperature Converter       | 02 - Currency Converter | 03 - Length Converter\n04 - Time and Duration Converter | 05 - Volume Converter   | 06 - Number Bases Converter\n07 - Digital Storage Converter   | 08 - Weight Converter   | 09 - Area Converter\n10 - Energy Converter            | 11 - Pressure Converter | 12 - Exit")
        try:
            option = int(input("Choose an option - "))
        except ValueError:
            print("Invalid option. Please, enter a number from 1 to 12.")
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
            run_digital_storage_converter()
        elif option == 8:
            run_weight_converter()
        elif option == 9:
            run_area_converter()
        elif option == 10:
            run_energy_converter()
        elif option == 11:
            run_pressure_converter()
        elif option == 12:
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()