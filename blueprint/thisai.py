import sys
import openai
from fpdf import FPDF

openai.api_key = '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'

input_string = ''

for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    input_string += arg


# Split the string into a list of key-value pairs
kv_pairs = input_string.split(', ')



def chatgpt(kv_pairs):
    # Loop through each key-value pair and extract the value for the desired keys
    title = ''
    subject = ''
    subtopics = ''

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


    ask = ('Question: can you write a response with a summary of' + title + subject + subtopics)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=150,
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



def add_text_to_pdf(title, subject, subtopics, text):
    # Define the page size and margins
    PAGE_WIDTH = 210
    LEFT_MARGIN = 20

    # Create a new PDF object
    pdf = FPDF()

    # Set the font and font size for the title, subject, and subtopics
    pdf.set_font('Arial', 'B', 16)

    # Add a new page to the PDF
    pdf.add_page()

    # Add the title to the top of the PDF
    pdf.cell(PAGE_WIDTH - LEFT_MARGIN * 2, 10, title, 0, 1, 'C')

    # Add the subject to one line below the title
    pdf.cell(PAGE_WIDTH - LEFT_MARGIN * 2, 10, subject, 0, 1, 'C')

    # Add the subtopics to one line below the subject
    pdf.cell(PAGE_WIDTH - LEFT_MARGIN * 2, 10, subtopics, 0, 1, 'C')

    # Set the font and font size for the text
    pdf.set_font('Arial', '', 12)

    # Add a line break between the subtopics and the text
    pdf.ln()

    # Create a multicell that spans the entire page and add the text to it
    pdf.multi_cell(PAGE_WIDTH - LEFT_MARGIN * 2, 10, text, 0, 'L')

    # Output the resulting PDF with the title, subject, subtopics, and text
    pdf.output('example.pdf', 'F')



add_text_to_pdf(title, subject, subtopics, text)