import wordninja
import sys
from fpdf import FPDF
from future import TriFoldPDF

# a function to unconcatenate the string and return w/ spaces
def stringSplit(conString):
    print('test')
    result = wordninja.split(conString)
    result = " ".join(result)
    return result

WIDTH = 210
HEIGHT = 297
MARGIN = 10

input_string = ''
file = open('argumentTest.txt', 'w')
for i in range(1, len(sys.argv)):
    file.write(sys.argv[i]+"\n")
    arg = sys.argv[i]
    input_string += arg
file.close()

# Split the string into a list of key-value pairs
kv_pairs = input_string.split(',')

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

# unconcatenate the dictionary
for key, value in input_dict.items(): 
    #if key == 'company':
        #pass
    if key == 'phone' or key=='email':
        pass 
    else:
        str_split = stringSplit(value)
        strc_split_dict = {key: str_split}
        input_dict.update(strc_split_dict)

# print results to txt file
with open ('inputTxtResult.txt', 'w') as f:
    for key, value in input_dict.items():
        f.write('%s:%s\n' % (key,value))

# Split the string for the necessary topics
###company = stringSplit(company)
###about = stringSplit(about)
###looking = stringSplit(looking)
###benefits = stringSplit(benefits)

###file = open('inputTxtResult.txt', 'w')
###file.write(company)
###file.write(about)
###file.write(looking)
###file.write(benefits)
###file.write(address)
###file.write(phone)
###file.write(email)
###file.close()

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def lines(self):
        self.set_line_width(0.0)
        self.line(0, HEIGHT / 3, WIDTH, HEIGHT / 3)
        self.line(0, 2 * HEIGHT / 3, WIDTH, 2 * HEIGHT / 3)


# Extract the values from the input_dict based on the keys
company = input_dict.get('company')
about = input_dict.get('about')
looking = input_dict.get('looking')
benefits = input_dict.get('benefits')
address = input_dict.get('address')
phone = input_dict.get('phone')
email = input_dict.get('email')
slogan = input_dict.get('slogan')

###class PDF(FPDF):
    ###def __init__(self, *args, **kwargs):
        ###super().__init__(*args, **kwargs)
        ###self.WIDTH = WIDTH
        ###self.HEIGHT = HEIGHT

    ###def lines(self):
        ###self.set_line_width(0.0)
        ###self.line(0, HEIGHT / 3, WIDTH, HEIGHT / 3)
        ###self.line(0, 2 * HEIGHT / 3, WIDTH, 2 * HEIGHT / 3)

# Create pdf output document
pdf = TriFoldPDF()
pdf.add_page()
# add content to pdf
pdf.draw_columns()
pdf.add_content('About Us', about,5,15)
pdf.add_content('Contact:', address,5, 80)
pdf.add_content(company, '',100,15)
pdf.add_content(slogan, '',100,25)
pdf.add_content('Benefits', benefits,200,15)
pdf.add_content('', email,200,90)
pdf.output('prof.pdf', 'F')

