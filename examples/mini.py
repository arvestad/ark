import ark
import csv


with open('tmp.csv') as h:
    reader = csv.reader(h, delimiter=',')
    a = ark.Ark(rows=reader, headers=0)

print(a)
