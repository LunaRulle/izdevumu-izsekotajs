import json
import os

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return False
    with open(EXPENSES_FILE, "r", encoding="utf-8") as user_file:
        return json.load(user_file)

def save_expenses(expenses):
    with open(EXPENSES_FILE, "r+", encoding="utf-8") as user_file:
        data = json.load(user_file)
        data.append(expenses)
        user_file.seek(0)
        user_file.write(json.dumps(data, indent=2, ensure_ascii=False))
