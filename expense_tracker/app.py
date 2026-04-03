from datetime import date, datetime
from storage import load_expenses, save_expenses
from logic import sum_total, sum_by_category, get_available_months, filter_by_month
from export import export_to_csv

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
            save_expenses(EXPENSES,True)
        else:
            exit()

def print_izdevumi(name=False,index=False,expenses=None):
    if name == True:
        print(f"{index}) Parādīt izdevumus")
        return
    else:
        print(f"Nr. {"Datums":<12}{"Kategorija":<15} {"Apraksts"} {"Summa":>10} ")
        print("-" * 50)
        if expenses == None:
            expenses = load_expenses()
        if type(expenses) == dict:
            print(f"{expenses["date"]:<12} {expenses["category"]:<15} {expenses["comment"]} {expenses["sum"]:>15.2f}€")
        else:
            for exp in expenses: #type: ignore
                index = index + 1
                print(f"{index}) {exp["date"]:<12} {exp["category"]:<15} {exp["comment"]} {exp["sum"]:>15.2f}€")
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
        print(f"{index}) Dzēst izdevumu")
        return
    else:
        expenses = load_expenses()
        print_izdevumi(expenses= expenses)
        print(f"izvēlaties kuru izdevumu dzēst (1-{len(expenses)}): >", end="") # type: ignore
        while True:
            try:
                user_choice = user_input("int")
                expenses[user_choice - 1] # type: ignore
                break
            except IndexError:
                print("Šī nav opcija")
                continue
        to_delete = expenses[user_choice -1] # type: ignore
        print_izdevumi(expenses= to_delete)
        print("Vai tiešām vēlies dzēst šo izdevumu? (y/n): >", end="")
        user_answer = user_input("bool")
        if user_answer == True:
            del expenses[user_choice - 1] # type: ignore
            print("Tagadējie izdevumi")
            print_izdevumi(expenses= expenses)
            save_expenses(expenses)
        else:
            exit()

def export(name=False,index=False):
    if name == True:
        print(f"{index}) Eksportēt uz csv")
        return
    else:
        print("Kā jūs vēaties nosaukt failu [izdevumi.csv]: > ", end="")
        expenses = load_expenses()
        while True:
            file_name = user_input("no")
            if export_to_csv(expenses, file_name) == False: # type: ignore
                print("Fails jau existē")
                continue
            else:
                print("Dokuments saglabāts")
                break


options = [add_izdevums, print_izdevumi, print_filter_by_month, total_by_catogry, delete_entry, export, end_session]

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
    main()
