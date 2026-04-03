from datetime import date, datetime
from storage import load_expenses, save_expenses
from logic import sum_total, sum_by_category, get_available_months, filter_by_month

CATEGORIES = [ 
    "Ēdiens", 
    "Transports", 
    "Izklaide", 
    "Komunālie maksājumi", 
    "Veselība", 
    "Iepirkšanās", 
    "Cits", 
] 

TODAY = date.today()

EXPENSES = {
    "date": "",
    "category": "",
    "comment": "",
    "sum": ""
}

def add_izdevums(name=False,index=False):
    if name == True:
        print(f"{index}) Pievienot Izdevumu")
        return

    else:
        print(f"Datums (YYYY-MM-DD) {TODAY} > ", end="")
        EXPENSES["date"] = str(user_input("time"))# type: ignore
        print("Kategorija:")

        for index, item in enumerate(CATEGORIES):
            print(f"{index + 1}) {item}")

        while True:
            try:
                print(f"Izēvlies (1-{len(CATEGORIES)}) > ", end="")
                category_index = user_input("int")
                EXPENSES["category"] = CATEGORIES[category_index - 1] # type: ignore
            except IndexError:
                print("Šī nav opcija")
                continue
            else:
                break

        print("Komentārs: > ", end="")
        EXPENSES["comment"] = user_input("no")# type: ignore
        
        print("Summa: > ", end="")
        EXPENSES["sum"] = user_input("float")# type: ignore

        print(f" {EXPENSES["date"]} | {EXPENSES["category"]} | {EXPENSES["comment"]} | {EXPENSES["sum"]:8.2f}€ ") # type: ignore

        print("Vai vēlies saglabāt datus? (y/n) > ", end="")
        answer = user_input("bool")
        if answer == True:
            save_expenses(EXPENSES)
        else:
            exit()

def print_izdevumi(name=False,index=False,expenses=None):
    if name == True:
        print(f"{index}) Parādīt izdevumus")
        return
    else:
        print(f"{"Datums":<12}{"Kategorija":<15} {"Apraksts"} {"Summa":>10} ")
        print("-" * 50)
        if expenses == None:
            expenses = load_expenses()
        for exp in expenses: #type: ignore
            print(f"{exp["date"]:<12} {exp["category"]:<15} {exp["comment"]} {exp["sum"]:>15.2f}€")
        print(f"Total sum: {sum_total(expenses):.2f}€")

def end_session(name=False,index=False):
    if name == True:
        print(f"{index}) Iziet nosaukums")
        return
    else:
        exit()

def print_filter_by_month(name=False,index=False):
    if name == True:
        print(f"{index}) Filtrēt pēc mēneša")
        return
    else:
        expenses = load_expenses()
        months = get_available_months(expenses)
        for month in months:
            index = index + 1
            print(f"{index}) {month}")
        print(f"Izvēlaties mēnesi ko apskatīt (1-{index}) > ", end="")
        while True:
            try:
                user_choice = user_input("int")
                user_month = datetime.strptime(months[user_choice - 1], "%Y-%m") # type: ignore
                break
            except IndexError:
                print("Šī nav opcija")
                continue
        filtered_expenses = filter_by_month(expenses, user_month.year, user_month.month)
        print_izdevumi(expenses=filtered_expenses)

def total_by_catogry(name=False,index=False):
    if name == True:
        print(f"{index}) Kopsavilkums pa kategorijām")
        return
    else:
        print(f"{"Kategorija":<15} {"Summa":>10}")
        expenses = load_expenses()
        by_catorgy = sum_by_category(expenses)
        for category, sum in by_catorgy.items():
            print(f"{category}: {sum:>10.2f}€")

def delete_entry(name=False,index=False):
    if name == True:
        print(f"{index}) Parādīt izdevumus")
        return
    else:
        pass


options = [add_izdevums, print_izdevumi, print_filter_by_month, total_by_catogry, delete_entry, end_session]

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
                user_input = user_input.date()
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
        print_options()
        print(f"Izvēlaties opciju (1-{len(options)}): > ", end="")
        try:
            user_choice = user_input("int")
            options[user_choice - 1]() # type: ignore
        except IndexError:
            print("Šī nav opcija")
            continue

if __name__ == "__main__":
    print_izdevumi()
    main()
