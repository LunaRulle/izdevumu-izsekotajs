from datetime import datetime

def sum_total(expenses):
    total = 0
    for exp in expenses: #type: ignore
        total = exp["sum"] + total
    return total
        
