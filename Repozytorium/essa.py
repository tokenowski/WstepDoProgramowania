'''
values = [10,20,30]
keys = ['ten','twenty','thirty']

# print(list(zip(keys,values)))
# D1= dict(zip(keys,values))
# D1 = {}
# for i in range(len(keys)):
#     D1[keys[i]] = values[i]

D1 = {keys[i]:values[i] for i in range(len(keys))}
print("D1 = ",D1)

D2 = dict(thirty = 30, fourty = 40, fifty = 50)
print("D2 = ",D2)

# D1.update(D2)
D3 = D1.copy()
D3.update(D2)
print("D3 = ",D3)
'''

sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

# for k in sample_dict.keys():
#    print (f'{k:<7} = {sample_dict[k]:>10}')

for k, v in sample_dict.items():
    print(f'{k:<10} = {v:>10}')

L = {'age', 'name'}
# D = {}
# for i in L: # i = 'age'
#     if i in sample_dict:
#         D[i] = sample_dict[i]

D = {i:sample_dict[i] for i in L if i in sample_dict}
print(D)

# for k in L:
#     if k in sample_dict:
#         sample_dict.pop(k)
# print(sample_dict)

# for k in L:
#     print(sample_dict.pop(k, 'Brak pary o danym kluczu'))

if 'Jones' in sample_dict.values():
    print("Wystepuje")
else: print('Brak')

sample_dict['location'] = sample_dict['city']
del sample_dict['location']
# sample_dict['location'] = sample_dict.pop('city', None)

print(sample_dict)