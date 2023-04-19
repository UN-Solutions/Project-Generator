import sys
from fpdf import FPDF

WIDTH = 210
HEIGHT = 297
MARGIN = 10

input_string = ''
for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    input_string += arg

# Split the string into a list of key-value pairs
kv_pairs = input_string.split(',')
print('test')
# print out kv paris i/p
file = open('kvpairs.txt','w')
for i in kv_pairs:
	file.write(i+"\n")
file.close()

# Create an empty dictionary to store the key-value pairs
input_dict = {}

# Loop through the input list and split each string by the delimiter ': ' to get the key-value pairs
for item in kv_pairs:
    key, value = item.split(': ')
    input_dict[key.strip()] = value.strip()

# output file of input text in a dictionary
with open("demofile2.txt", 'w') as f: 
    for key, value in input_dict.items(): 
        f.write('%s:%s\n' % (key, value))

# Extract the values from the input_dict based on the keys
company = input_dict.get('company')
about = input_dict.get('about')
looking = input_dict.get('looking')
benefits = input_dict.get('benefits')
address = input_dict.get('address')
phone = input_dict.get('phone')
email = input_dict.get('email')

file = open('inputTxtResult.txt', 'w')
file.write(company)
file.close()

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def lines(self):
        self.set_line_width(0.0)
        self.line(0, HEIGHT / 3, WIDTH, HEIGHT / 3)
        self.line(0, 2 * HEIGHT / 3, WIDTH, 2 * HEIGHT / 3)


# Create the PDF object
pdf = PDF(orientation='L')
pdf.add_page()

# Add the content to the PDF object
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, company, 0, 1, 'C')
# pdf.cell(0, 10, slogan, 0, 1, 'C')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, about, 0, 1, 'L')
pdf.cell(0, 10, looking, 0, 1, 'L')
pdf.cell(0, 10, benefits, 0, 1, 'L')
pdf.cell(0, 10, address, 0, 1, 'L')
pdf.cell(0, 10, phone, 0, 1, 'L')
pdf.cell(0, 10, email, 0, 1, 'L')

# Add the lines to the PDF object
pdf.lines()

# Save the PDF file
pdf.output('prof.pdf', 'F')



