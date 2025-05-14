import ark
import csv

def row_conversion(lst):
    passenger_id, survived, p_class, p_name, sex, age, sib_sp, parch, ticket, fare, cabin, embarked = lst
    if age:
        try:
            age = int(age)
        except ValueError:
            age = float(age)
    return int(passenger_id), int(survived), int(p_class), p_name, sex, age, int(sib_sp), int(parch), ticket, float(fare), cabin, embarked


with open('titanic.csv') as h:
    headers = h.readline().split(',')
    reader = csv.reader(h, delimiter=',')
    rows = list(map(row_conversion, reader))
    titanic = ark.Ark(rows=rows, headers=headers)

print(titanic.head(5))
