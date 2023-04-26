import sys
import openai
from fpdf import FPDF
import re

openai.api_key = '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'
input_string = ''
for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    input_string += arg

# Split the string into a list of key-value pairs
kv_pairs = input_string.split(',')

class TriFoldPDF(FPDF):
    pass

    def __init__(self):
        super().__init__(orientation = 'L') # Set the orientation
        self.page_size = (279.4, 215.9) # A4 paper size in mm 1056x816 pixels
        self.left_margin = 1 # mm
        self.right_margin = -16 # mm
        self.top_margin = 1 # mm
        self.bottom_margin = 10 # mm
        self.column_gap = 0 # mm
        self.column_width = (self.page_size[0] - self.left_margin - self.right_margin - self.column_gap*2) / 3

    def draw_columns(self):
        x = self.left_margin
        y = self.top_margin
        for i in range(3):
            self.rect(x, y, self.column_width, self.page_size[1] - self.top_margin - self.bottom_margin, 'D')
            x += self.column_width + self.column_gap

    def get_multiline_cell_height(self, width, text):
        lines = text.split('\n')
        total_height = 0
        for line in lines:
            line_width = self.get_string_width(line)
            if line_width <= width:
                total_height += self.font_size
            else:
                # calculate height of line with word wrap
                words = line.split()
                line = ''
                for word in words:
                    if self.get_string_width(line + ' ' + word) <= width:
                        line += ' ' + word
                    else:
                        total_height += self.font_size
                        line = word
                total_height += self.font_size
        return total_height


    def add_content(self, title, body, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', 'B', 14)
        self.cell(self.column_width - 10, 10, title, 0, 1)
        self.set_xy(x, y + 8)
        self.set_font('Arial', '', 8)
        cell_width = self.column_width - 9
        cell_height = self.get_multiline_cell_height(cell_width, body)
        self.multi_cell(self.column_width - 9, 8, body)
        
    def add_bullet_content(self, title, body, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', 'B', 14)
        self.cell(self.column_width - 10, 10, title, 0, 1)
        self.set_xy(x, y)
        self.set_font('Arial', '', 8)
        cell_width = self.column_width - 9
        cell_height = self.get_multiline_cell_height(cell_width, body)
        self.multi_cell(self.column_width - 9, 8, body)


title = "Car Emissions"
def chatgpt(kv_pairs):
    # Loop through each key-value pair and extract the value for the desired keys
    title = 'Cigarette'
    subject = 'Harm of Cigarettes'
    subtopics = 'Human body'

    for kv in kv_pairs:
        if 'title:' in kv:
            title = kv.split(':')[1]
        elif 'subject:' in kv:
            subject = kv.split(': ')[1]
        elif 'subtopics:' in kv:
            subtopics = ':'.join(kv.split(':')[1:])

    # Print the extracted values
    print('Title:', title)
    print('Subject:', subject)
    print('Subtopics:', subtopics)

    ask = ('Can you write a report with the main title going to be '+ title + ', and the main subject matter is about the ' + subject + ' with subtopics of ' + subtopics + '. could you give me an Problems & Affects, Background Research, Prevention Steps, and a Conclusion section. If you could give both the  Problema & Affects and prevention steps as a list with each point starting with "-". add a double enter at the end of each section. use a ":" behind the title of sections. I do not need a main title given. Start with Problems & Affects, have the background research be one paragarph around 100 words, and the Conclusion be under 250 characters.')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=700,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    print('Title:', title)
    text = response['choices'][0]['text']
    print('Reply:' + text)

    return text, title, subject, subtopics

text, title, subject, subtopics = chatgpt(kv_pairs)

sections = text.split('\n\n')
problems_and_affects = sections[1]
problems_and_affects = re.sub(r"Problems & Affects:", "", problems_and_affects)
background_research = sections[2]
background_research = re.sub(r"Background Research:", "", background_research)
prevention_steps = sections[3]
prevention_steps = re.sub(r"Prevention Steps:", "", prevention_steps)
conclusion = sections[4]
conclusion = re.sub(r"Conclusion:", "", conclusion)

# Check if the first line starts with a newline character
if background_research.startswith('\n'):
    # If the first line starts with a newline character, remove it
    background_research = background_research[1:]

# Check if the first line starts with a newline character
if conclusion.startswith('\n'):
    # If the first line starts with a newline character, remove it
    conclusion = conclusion[1:]

print(problems_and_affects)
print(background_research)
print(prevention_steps)
print(conclusion)


pdf = TriFoldPDF()
pdf.add_page()
# Add the title to the top of the PDF
pdf.draw_columns()
pdf.add_bullet_content('Problems & Affects', problems_and_affects,5,30)
pdf.add_content('Background Research', background_research,100, 40)
pdf.add_content(title, '',100,15)
pdf.add_bullet_content('Prevention Steps', prevention_steps,200,15)
pdf.add_content('Conclusion', conclusion,200,120)
pdf.output('awareness.pdf', 'F')
