import pandas as pd
from ark import Ark, ArkRow

print('# Import with pandas:')
df = pd.read_csv('tmp.csv')
print(df)

print('# Import with Ark:')
import csv
with open('tmp.csv') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    a = Ark(reader, headers=0)
print(a)

print('\n------------\n')

r1 = ArkRow([1,2,3])
r2 = ArkRow([3,2,1])
print(r1 + r2)

print('------------')

print(0 + r1)

# for row in a:
#     print(row)
    
print(sum(a))
print('\n------------\n')

print('Count rows grouped by elements in column 1:')
import itertools as it
for k, g in it.groupby(a, a.column(0)):
    print(k, len(list(g)))
    
print('Sum rows grouped by elements in column 1:')
import itertools as it
for k, g in it.groupby(a, a.column(0)):
    print(k, sum(g))
    
