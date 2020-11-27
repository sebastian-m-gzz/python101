import csv


def read(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            print(line)


def read_to_dict(path):
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for line_map in reader:
            print(line_map)
