import sys
from readtxt import getText
import openai
from fpdf import FPDF
import re
import unicodedata
# openai key from document when running web app, scope is within blueprint directory
file = open("keys_for_car.txt")
openai.api_key = file.read()

# Get user input
input_string = getText('inputpres.txt')
kv_pairs = input_string
# kv_pairs = input_string.split(',')

class PowerPointPDF(FPDF):

    def __init__(self):
        super().__init__('L', 'in', (7.5, 10))  # Landscape orientation, inches as units, and custom page size
        self.set_margins(0.5, 0.5, 0.5)  # Set 0.5-inch margins

    def draw_border(self):
        self.set_line_width(0.05)  # Set the line width for the border
        self.rect(0.5, 0.5, 9, 6.5)  # Draw a rectangle as the border

    def sanitize_text(self, text):
        return ''.join(c for c in unicodedata.normalize('NFKD', text) if ord(c) < 256)
    def add_slide(self, title, content):
        self.add_page()
        self.draw_border()
        self.set_font("Comic", 'B', 24)  # Set the font for the title
        self.set_xy(1, 1)  # Set the position for the title
        self.cell(8, 1, title, 0, 1, 'C')  # Add the title

        self.set_font("Comic", '', 12)  # Set the font for the content
        self.set_xy(1, 2)  # Set the position for the content
        content = self.fit_text_to_slide(content)
        self.multi_cell(8, 0.5, content, 0, 'C')  # Add the content

    def fit_text_to_slide(self, text):
        max_lines = int((6.5 - 2) / 0.5)  # Calculate the maximum number of lines that can fit in the slide
        lines = text.split('\n')
        if len(lines) > max_lines:
            lines = lines[:max_lines]
            lines[-1] = lines[-1].rstrip() + '...'  # Add an ellipsis to the last line
            text = '\n'.join(lines)
        return text

def chatgpt(kv_pairs):
    # Loop through each key-value pair and extract the value for the desired keys
#     title = ''
#     subject = ''
#     subtopics = ''
#
#     for kv in kv_pairs:
#         if 'title:' in kv:
#             title = kv.split(':')[1]
#         elif 'subject:' in kv:
#             subject = kv.split(': ')[1]
#         elif 'subtopics:' in kv:
#             subtopics = ':'.join(kv.split(':')[1:])
    title = input_string['title']
    subject = input_string['subject']
    subtopics = input_string['subtopics']

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
pdf = PowerPointPDF()

# Add slides with titles and content
pdf.add_slide(title, subject)
pdf.add_slide("", background)
pdf.add_slide("", results)
pdf.add_slide("", conclusion)

pdf.output("presentation.pdf", "F")

