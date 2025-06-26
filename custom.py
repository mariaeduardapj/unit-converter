def run_custom_converter():
    a = "Variable_A"
    b = "Variable_B"
    op = ["plus","minus","times","divided","raised"]
    functions_a_to_b = lambda x: x * 1
    functions_b_to_a = lambda x: x * 1
    print("-=-=-=-=-=- CUSTOM CONVERTER -=-=-=-=-=-")
    while True:
        print("Variable_A = 1 * Variable_B\nVariable_B = 1 * Variable_A")
        print("Menu options:\n2 - Rename Variable | 3 - Change Conversion Function | 4 - End")
        try:
            o = int(input("> "))
            if not (1 <= o <= 4):
                print("Invalid option. Please choose a number between 1 and 4.")
                return
        except ValueError:
            print("Invalid option. Please, enter a number from 1 to 4.")
            exit()
        if o == 1:
            print(f"Converted:\n1 - {a} to {b} | 2 - {b} to {a}")
            try:
                c = int(input("> "))
                if not (1 <= 1 <= 2):
                    print("Invalid option. Please choose a number between 1 and 2.")
            except ValueError:
                print("Invalid option. Please, enter a number from 1 to 2.")
                exit()
            if c == 1:
                value = float(input(f"Value in {a} - "))
                print(f"{value} {a} -> {functions_a_to_b(value)} {b}")
            elif c == 2:
                value = float(input(f"Value in {b} - "))
                print(f"{value} {b} -> {functions_b_to_a(value)} {a}")
        elif o == 2:
            try:
                r = int(input(f"Rename:\n 1 - {a} | 2 - {b}\n> "))
                if not (1 <= o <= 2):
                    print("Invalid option. Please choose a number between 1 and 2.")
            except ValueError:
                print("Invalid option. Please, enter a number from 1 to 2.")
                exit()
            if r == 1:
                a = input(f"New name of {a} - ")
            elif r == 2:
                b = input(f"New name of {b} - ")
        elif o == 3:
            try:
                r = int(input(f"Change function:\n {a} to {b} | {b} to {a}\n> "))
                if not (1 <= o <= 2):
                    print("Invalid option. Please choose a number between 1 and 2.")
            except ValueError:
                print("Invalid option. Please, enter a number from 1 to 2.")
                exit()
            if r == 1:
                print(f"{b} = {a} ...\n1 - Plus | 2 - Minus | 3 - Times | 4 - Divided | 5 - Raised")
                try:
                    oper = int(input("> "))
                    if not (1 <= o <= 5):
                        print("Invalid option. Please choose a number between 1 and 5.")
                except ValueError:
                    print("Invalid option. Please, enter a number from 1 to 5.")
                    exit()
                print(f"{b} = {a} {op[oper-1]} ...")
                try:
                    value = float(input("> "))
                except ValueError:
                    print("Invalid option. Please, enter a number.")
                    exit()
                if oper == 1:
                    functions_a_to_b = lambda x: x + value
                elif oper == 2:
                    functions_a_to_b = lambda x: x - value
                elif oper == 3:
                    functions_a_to_b = lambda x: x * value
                elif oper == 4:
                    functions_a_to_b = lambda x: x / value
                elif oper == 5:
                    functions_a_to_b = lambda x: x ** value
            elif r == 2:
                print(f"{a} = {b} ...\n1 - Plus | 2 - Minus | 3 - Times | 4 - Divided | 5 - Raised")
                try:
                    oper = int(input("> "))
                    if not (1 <= o <= 5):
                        print("Invalid option. Please choose a number between 1 and 5.")
                except ValueError:
                    print("Invalid option. Please, enter a number from 1 to 5.")
                    exit()
                print(f"{a} = {b} {op[oper - 1]} ...")
                try:
                    value = float(input("> "))
                except ValueError:
                    print("Invalid option. Please, enter a number.")
                    exit()
                if oper == 1:
                    functions_b_to_a = lambda x: x + value
                elif oper == 2:
                    functions_b_to_a = lambda x: x - value
                elif oper == 3:
                    functions_b_to_a = lambda x: x * value
                elif oper == 4:
                    functions_b_to_a = lambda x: x / value
                elif oper == 5:
                    functions_b_to_a = lambda x: x ** value
        elif o == 4:
            break