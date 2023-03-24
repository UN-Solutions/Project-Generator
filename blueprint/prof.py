import sys
import openai
from fpdf import FPDF

openai.api_key = ''
input_string = ''
for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    input_string += arg

# Split the string into a list of key-value pairs
kv_pairs = input_string.split(',')