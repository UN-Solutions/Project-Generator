from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import os

# Define the PDF document
file_path = os.path.join("public", "example.pdf")
doc = SimpleDocTemplate(file_path, pagesize=landscape(letter), rightMargin=inch/2, leftMargin=inch/2, topMargin=inch/2, bottomMargin=inch/2)
elements = []

# Add the title to the PDF
title_style = ParagraphStyle(name='Title', fontSize=16, leading=24, alignment=1, spaceAfter=24)
title_text = '<strong>My PDF Title</strong>'
title = Paragraph(title_text, title_style)
elements.append(title)

# Add the two columns to the PDF
column_style = ParagraphStyle(name='Column', fontSize=12, leading=18, spaceAfter=12)
data = [
    ['Column 1, Row 1', 'Column 2, Row 1'],
    ['Column 1, Row 2', 'Column 2, Row 2'],
    ['Column 1, Row 3', 'Column 2, Row 3'],
]
table = Table(data)
table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                           ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('FONT', (0, 0), (-1, -1), 'Helvetica', 12),
                           ('LINEBELOW', (0, 0), (-1, 0), 1, (0, 0, 0)),
                           ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                           ('BACKGROUND', (0, 1), (-1, 1), (0.9, 0.9, 0.9)),
                           ('BACKGROUND', (0, 2), (-1, 2), (0.8, 0.8, 0.8))]))
elements.append(table)

# Add a spacer to the end of the PDF
spacer = Spacer(1, inch/2)
elements.append(spacer)

# Build the PDF document and save it
doc.build(elements)
