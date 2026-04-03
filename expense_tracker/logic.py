from datetime import datetime

def sum_total(expenses):
    total = 0
    for exp in expenses: #type: ignore
        total = exp["sum"] + total
    return total
       
def sum_by_category(expenses):
    totals = {}
    for exp in expenses: 
        cat = exp["category"]
        totals[cat] = totals.get(cat, 0) + exp["sum"]
    return {cat: total for cat, total in totals.items()}

def get_available_months(expenses):
    months = []
    for exp in expenses:
        dates = datetime.strptime(exp["date"], "%Y-%m-%d")
        month = datetime.strftime(dates, "%Y-%m")
        if month not in months:
            months.append(month)
    return months


