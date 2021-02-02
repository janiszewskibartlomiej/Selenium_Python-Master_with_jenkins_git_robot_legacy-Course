# Nested Dictionary

odics = {'k1': {'id': 21, 'name': 'A'},
         'k2': {'id': 22, 'name': 'B'},
         'k3': {'id': 23, 'name': 'C'}
         }

# Fetch value from Nested Dictionary
print(odics['k1']['id'])
print(odics['k3']['name'])

# Adding value to main dictionary
odics['k4'] = {'id': 24, 'name': 'D'}
print(odics)

# Add Value to internal dictionary
odics['k3']['test'] = "testing"
print(odics)

# Update Value
odics['k2']['name'] = "ZZ"
print(odics)
