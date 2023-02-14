import sys
import openai


input = sys.argv[1]
input2 = sys.argv[2]
input3 = sys.argv[3]

input_string = (input + " " + input2 + " " + input3)


# Split the string into a list of key-value pairs
kv_pairs = input_string.split(', ')

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


openai.api_key = "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"

ask = ('Question: can you write a summary about ' + title)
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

text = response['choices'][0]['text']
print ('Reply: '+text)
