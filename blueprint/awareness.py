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
        self.set_xy(x, y + 12)
        self.set_font('Arial', '', 8)
        cell_width = self.column_width - 9
        cell_height = self.get_multiline_cell_height(cell_width, body)
        self.multi_cell(self.column_width - 9, 8, body)


title = "Car Emissions"
def chatgpt(kv_pairs):
    # Loop through each key-value pair and extract the value for the desired keys
    title = ''
    subject = ''
    subtopics = ''

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

    ask = ('Can you write a report with the main title going to be '+ title + ', and the main subject matter is about the ' + subject + ' with subtopics of ' + subtopics + '. could you give me an abstract, background research, results, a conclusion, and a future directions section. add a double enter at the end of each section. use a ":" behind the title of sections. I do not need a main title given.')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=1000,
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


# Define regular expression patterns to match the section titles
abstract_pattern = re.compile(r"Abstract:\s*(.*)\n\n")
background_pattern = re.compile(r"Background Research:\s*(.*)\n\n")
results_pattern = re.compile(r"Results:\s*(.*)\n\n")
conclusion_pattern = re.compile(r"Conclusion:\s*(.*)\n\n")
future_pattern = re.compile(r"Future Directions:\s*(.*)")

# Extract the text for each section
abstract = abstract_pattern.search(text).group(1)
background = background_pattern.search(text).group(1)
results = results_pattern.search(text).group(1)
conclusion = conclusion_pattern.search(text).group(1)
future = future_pattern.search(text).group(1)

# Print the results
print("Abstract:", abstract)
print("Background Research:", background)
print("Results:", results)
print("Conclusion:", conclusion)
print("Future Directions:", future)


pdf = TriFoldPDF()
pdf.add_page()
# Add the title to the top of the PDF
pdf.draw_columns()
pdf.add_content('Abstract', abstract,5,15)
pdf.add_content('Background Research:', background,5, 80)
pdf.add_content(title, '',100,15)
pdf.add_content('Results', results,100,25)
pdf.add_content('Conclusion', conclusion,200,15)
pdf.add_content('Future Directions', future,200,90)
pdf.output('awareness.pdf', 'F')
