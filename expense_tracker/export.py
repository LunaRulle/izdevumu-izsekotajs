import csv
import os

def export_to_csv(expenses, name="izdevumi.csv"):
    if os.path.exists(name):
        return False
    else:
        with open(name, "x", newline="", encoding="utf-8-sig") as user_file:
            writer = csv.writer(user_file)
            header = True
            for data in expenses:
                if header == True:
                    keys = data.keys()
                    writer.writerow(keys)
                    header = False
                writer.writerow(data.values())



        
