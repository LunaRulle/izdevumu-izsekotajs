from datetime import date, datetime
from storage import load_expenses, save_expenses

CATEGORIES = [ 
    "Ēdiens", 
    "Transports", 
    "Izklaide", 
    "Komunālie maksājumi", 
    "Veselība", 
    "Iepirkšanās", 
    "Cits", 
] 

def add_izdevums(name,index):
    if name == True:
        print(f"{index}) Pievienot Izdevumu")
        return
    else:
        print("izdevums pievienots")

def print_izdevumi(name,index):
    if name == True:
        print(f"{index}) Parādīt izdevumus")
        return
    else:
        print("izdevums parādīts ")
def end_session(name,index):
    if name == True:
        print(f"{index}) Iziet nosaukums")
        return
    else:
        exit()

options = [add_izdevums, print_izdevumi, end_session]

def print_options():
    for index, item in enumerate(options):
        name = True
        item(name, index + 1)

def user_input(validation):
    while True:
        user_input = "" 
        if validation == "no":
            user_input = input()
        elif validation == "int":
            try:
                user_input = int(input())
            except ValueError:
                print("Lūdzu ierakstiet vesalu skaitli")
                continue
        elif validation == "float":
            try:
                user_input = float(input())
            except ValueError:
                print("Lūdzu ierakstiet skaitli")
                continue
        elif validation == "bool":
            user_input = input().lower().startswith("y")
        elif validation == "time":
            try:
                user_input = datetime.strptime(input(), "%Y-%m-%d")
            except ValueError:
                print("Tas nav pareiz laika formāts, lūdzu rasktiet YYYY-MM-DD formātā")
                continue
        return user_input

def main():
    if load_expenses() == False:
        print(f"Nav atrasts expenses.json, vai vēlies uztaisīt jaunu? (y/n)", end=" ")
        answer = user_input("bool")
        if answer == True:
            save_expenses([])
        if answer == False:
            exit()
    while True:
        print(f"Izvēlaties opciju (1-{len(options)})")
        print_options()
        try:
            user_choice = user_input("int")
            options[user_choice - 1](False,False) # type: ignore
        except IndexError:
            print("Šī nav opcija")
            continue

if __name__ == "__main__":
    main()
