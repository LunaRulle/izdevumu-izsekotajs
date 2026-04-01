from storage import load_expenses

def sum_total():
    data = load_expenses()
    total = 0
    for exp in data: #type: ignore
        total = exp["sum"] + total
    return total
        
