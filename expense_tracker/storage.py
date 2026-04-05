import json
import os
import operator

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return False
    with open(EXPENSES_FILE, "r", encoding="utf-8") as user_file:
        return json.load(user_file)

def save_expenses(expenses,append=False):
    if append == True:
        with open(EXPENSES_FILE, "r+", encoding="utf-8") as user_file:
            data = json.load(user_file)
            data.append(expenses)
            user_file.seek(0)
            user_file.write(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        with open(EXPENSES_FILE, "w", encoding="utf-8") as user_file:
            user_file.seek(0)
            user_file.write(json.dumps(expenses, indent=2, ensure_ascii=False))

def sort_expenses(expenses):
    with open(EXPENSES_FILE, "w", encoding="utf-8") as user_file:
        expenses = sorted(expenses, key=operator.itemgetter("date"), reverse= True) #type: ignore
        user_file.write(json.dumps(expenses, indent=2, ensure_ascii=False))

