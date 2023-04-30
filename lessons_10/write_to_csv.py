import csv


def write_to_csv_file(data_list: list):
    with open('Exchange rate for the period.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data_list)
    return print('Data saved to file: "Exchange rate for the period"!')
