import json
from readtxt import getText
from fpdf import FPDF
from future import TriFoldPDF

#### Extract the values from the input_dict based on the keys
###company = input_dict.get('company')
###about = input_dict.get('about')
###looking = input_dict.get('looking')
###benefits = input_dict.get('benefits')
###address = input_dict.get('address')
###phone = input_dict.get('phone')
###email = input_dict.get('email')
###slogan = input_dict.get('slogan')

# Get user input
profInputs = getText('input.txt')
#store user input for pdf
company = profInputs['company']
about = profInputs['about']
looking = profInputs['address']
benefits = profInputs['benefits']
address = profInputs['address']
phone = profInputs['phone']
email = profInputs['email']
slogan = profInputs['slogan']

# Create pdf output document
pdf = TriFoldPDF()
pdf.add_page()
# add content to pdf
pdf.draw_columns()
# First Section
pdf.add_content('About Us', about,5,15)
pdf.add_content('Contact:', address,5, 155)
pdf.add_content('',email,5, 160)
pdf.add_content('',phone,5, 165)
# Second Section
pdf.add_content(company, '',100,15)
pdf.add_content(slogan, '',100,25)
# Third Section
pdf.add_content('Benefits', benefits,200,15)
pdf.add_content('Looking For', looking,200,110)
pdf.output('prof.pdf', 'F')

