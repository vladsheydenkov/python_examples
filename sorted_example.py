"""sorted func example"""
import operator

unsorted_list = [
    {'name': 'Bob', 'age': 35},
    {'name': 'Adam', 'age': 23},
    {'name': 'Abc', 'age': 66},
]
print(unsorted_list)
sorted_list = sorted(list_, key=operator.itemgetter('name', 'age'))
print(sorted_list)
