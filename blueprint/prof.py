import sys
from fpdf import FPDF

input_string = ''
for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    input_string += arg

# Split the string into a list of key-value pairs
kv_pairs = input_string.split(',')
print('test')

# Create an empty dictionary to store the key-value pairs
input_dict = {}

# Loop through the input list and split each string by the delimiter ': ' to get the key-value pairs
for item in kv_pairs:
    key, value = item.split(': ')
    input_dict[key.strip()] = value.strip()


# Extract the values from the input_dict based on the keys
company = input_dict.get('company')
about = input_dict.get('about')
looking = input_dict.get('looking')
benefits = input_dict.get('benefits')
address = input_dict.get('address')
phone = input_dict.get('phone')
email = input_dict.get('email')



