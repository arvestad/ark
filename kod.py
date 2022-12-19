import pandas as pd
import ark

df = pd.read_csv('tmp.csv')

print('Pandas:')
print(df)

a = Ark.read_csv('tmp.csv')
print(a)

r1 = ArkRow([1,2,3])
r2 = ArkRow([3,2,1])
print(r1 + r2)

print('--- --- --- ---')

print(0 + r1)

# for row in a:
#     print(row)
    
#print(sum(a))
