import ark
import csv
import itertools as it
import ark.statistics as stat
import ark.tools as tools

titanic_file = '10rows_titanic.csv'

def row_conversion(lst):
    passenger_id, survived, p_class, p_name, sex, age, sib_sp, parch, ticket, fare, cabin, embarked = lst
    if age:
        try:
            age = int(age)
        except ValueError:
            age = float(age)
    return int(passenger_id), int(survived), int(p_class), p_name, sex, age, int(sib_sp), int(parch), ticket, float(fare), cabin, embarked


with open(titanic_file) as h:
    headers = h.readline().split(',')
    reader = csv.reader(h, delimiter=',')
    rows = list(map(row_conversion, reader))
    titanic = ark.Ark(rows=rows, headers=headers)

print('First 5 rows of data:')
print(titanic.head(5))

# print('All:')
# print(titanic)

print()
print('Sort by age and then show first 5 passengers:')
sorted_rows = sorted(titanic, key=titanic.column('Age', numeric=True))
for row in sorted_rows:
    print(row[3])

# print('mapping?')
# print(list(map(lambda r: (titanic.column('Sex')(r), r), titanic)))

#print(list(tools.collect_by(titanic, titanic.column('Sex'))))

print()
print('# Mean age for men and women')
age_sex = titanic[('Sex', 'Age')]

for sex, rows in tools.collect_by(age_sex, age_sex.column('Sex')):
    print(stat.mean(rows))
    
quit()

print('# Over 35')
for row in filter(lambda r: type(r['Age']) == int and r['Age'] >= 35, titanic):
    print(row)

