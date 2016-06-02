import csv

with open('store_todos.csv', 'r') as f:
    reader = list(csv.reader(f))
    for i in reader:
        for j in i:
            if j == 'True':
                print('[x]')
            elif j == 'False':
                print('[ ]')
