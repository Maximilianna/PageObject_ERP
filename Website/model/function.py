import csv

def get_data_csv():
    list = []
    steam = open(f"..\\test_data\\add_Commodity_Test.csv")
    reader = csv.reader(steam)
    for row in reader:
        list.append(row)
    return list
