import sys
import openai
from fpdf import FPDF
import re

openai.api_key = "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"

input_string = ''
for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    input_string += arg

# Split the string into a list of key-value pairs
kv_pairs = input_string.split(', ')

title = 'Main title'
class TriFoldPDF(FPDF):
    pass

    def __init__(self):
        super().__init__(orientation = 'L') # Set the orientation
        self.page_size = (279.4, 215.9) # A4 paper size in mm
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

    def add_content(self, title, body, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', 'B', 14)
        self.cell(self.column_width - 10, 10, title, 0, 1)
        self.set_xy(x, y + 5)
        self.set_font('Arial', '', 8)
        self.multi_cell(self.column_width - 9, 8, body)
        
def chatgpt(kv_pairs):
    # Loop through each key-value pair and extract the value for the desired keys
    title = 'Car Emissions'
    subject = 'Harm of car emissions'
    subtopics = 'CO2 and GHG'

    for kv in kv_pairs:
        if 'title:' in kv:
            title = kv.split(': ')[1]
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

# Sample text
# text = "Abstract: This report seeks to analyze the harm of car emissions, particularly focusing on carbon dioxide (CO2) and greenhouse gases (GHGs). It provides an overview of the current research on the topic as well as the potential consequences of excessive emissions. Lastly, it also gives recommendations for how to reduce emissions in order to avoid further damage.\n\nBackground Research: Cars have been a source of pollution for decades. The primary pollutants from automobiles are carbon dioxide (CO2) and greenhouse gases (GHGs) which are a major contributor to climate change. Additionally, vehicle exhaust is also harmful to the health of people living in areas with high levels of traffic. It can be inhaled and cause respiratory problems such as asthma or bronchitis.\n\nResults: Studies have shown that cars account for about 30% of all CO2 and GHG emissions worldwide. This means that any measures taken to reduce emissions from cars can have a significant impact on overall global emissions. One example of this is electric cars which produce significantly less emissions than gasoline-powered vehicles.\n\nConclusion: In conclusion, cars are one of the biggest sources of CO2 and GHG emissions and can cause serious health problems in areas with high levels of traffic. It is therefore important to take measures to reduce emissions from cars. This can be achieved through the adoption of electric vehicles, stricter emissions standards, more efficient driving techniques, and other measures designed to limit emissions.\n\nFuture Directions: Going forward, it will be important to continue researching ways to reduce emissions from cars. Governments and industries should work together to develop new technologies and regulations that can help to reduce the environmental impact of cars. Additionally, public education efforts should be undertaken in order to spread awareness of the issue and encourage people to take steps to reduce their own emissions."

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
pdf.add_content('Background Research:', background,5,90)
pdf.add_content(title, '',100,15)
pdf.add_content('Results', results,100,25)
pdf.add_content('Conclusion', conclusion,200,15)
pdf.add_content('Future Directions', future,200,90)
pdf.output('example.pdf', 'F')