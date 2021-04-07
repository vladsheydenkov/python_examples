"""Dictionary views dynamically reflect changes made to the dict 
after the view object has been created
"""
test_dict = dict(name='Bob')
test_keys = test_dict.keys()
test_values = test_dict.values()
print(test_keys, test_values)
del test_dict['name']
print(test_keys, test_values) 
