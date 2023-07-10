from ValidationException import ValidationException
import csv

def validate_file(file_path):
    row_list = []
    with open(file_path) as csv_file:
        # skip the first row
        next(csv_file)
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            row_list.append(row)
    for row in row_list:
        if any(char.isdigit() for char in row[0]):
            raise ValidationException(f"Invalid first name: {row[0]}" )

            
def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
