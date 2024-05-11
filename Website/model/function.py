import csv

def get_data_csv(str):
    list = []
    steam = open(str)
    reader = csv.reader(steam)
    for row in reader:
        list.append(row)
    return list
