import csv

def get_csv_data(filename):
    data_from_csv = []
    with open(filename, 'r', encoding='utf-8') as file:
