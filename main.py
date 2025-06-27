from temperature import run_temperature_converter
from currency import run_currency_converter
from converter_logic.length import run_length_converter
from time_duration import run_time_duration_converter
from converter_logic.volume import run_volume_converter
from number_bases import run_number_bases_converter
from digital_storage import run_digital_storage_converter
from weight import run_weight_converter
from area import run_area_converter
from energy import run_energy_converter
from pressure import run_pressure_converter
from frequency import run_frequency_converter
from custom import run_custom_converter

def main():
    while True:
        print()
        print("UNIT CONVERTER\n01 - Temperature Converter       | 06 - Number Bases Converter    | 11 - Pressure Converter\n02 - Currency Converter          | 07 - Digital Storage Converter | 12 - Frequency Converter\n03 - Length Converter            | 08 - Weight Converter          | 13 - Custom Converter\n04 - Time and Duration Converter | 09 - Area Converter            | 12 - Frequency Converter\n05 - Volume Converter            | 10 - Energy Converter")
        try:
            option = int(input("Choose an option - "))
            if not (1 <= option <= 14):
                print("Invalid option. Please, choose a number between 1 and 14.")
                return
        except ValueError:
            print("Invalid option. Please, enter a number from 1 to 14.")
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
            run_frequency_converter()
        elif option == 13:
            run_custom_converter()
        elif option == 14:
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()