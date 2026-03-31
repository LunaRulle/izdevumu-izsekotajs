import json
import os
# from app import user_input

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return False
    with open(EXPENSES_FILE, "r", encoding="utf-8") as user_file:
        return json.load(user_file)

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w", encoding="utf-8") as user_file:
        json.dump(expenses, user_file, indent=2, ensure_ascii=False)

