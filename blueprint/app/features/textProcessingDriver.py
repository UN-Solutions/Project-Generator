#TODO: Driver module that takes in text and outputs the various objects into a file
from textProcessing import TextProcessing
import re

# read in file 
pathCorrect = 'data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
##pathMore = '/home/msalvador45/school/spring23/seniorXP/project/Project-Generator/data/sampleTexts/longSumm.txt'
##pathLess = '/home/msalvador45/school/spring23/seniorXP/project/Project-Generator/data/sampleTexts/shortSumm.txt'
path = pathCorrect

with open(path) as f:
    ogText = f.read()
    f.close()

ogText = ogText.split() #create a list out of the text
print('the text has a lenght of: ', len(ogText),'words')

# Throw exceptions for insufficient word lenght or too much word length

if len(ogText) < 100 :
    raise Exception('text document is less than 100 words, need text document (100<length<2400)')
elif len(ogText) > 2400:
    raise Exception('text document is more than 2400 words, need text document (100<length<2400)')
else:
    print('text document is between 100 and 2400 words')
    fullText = ' '.join(ogText)
    
# create a list to store diff. sections of a text cut into fourths 
senList = re.split(r'[.!?]+',fullText)      #make a list out of all sentences in text doc
print('the number of sentences in text document is: ',len(senList),'sentences\n')   #number of sentences in doc

# code by user Adam Smith on https://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts
# function makes number of sections of a string
def chunk(in_string,num_chunks):
    chunk_size = len(in_string)//num_chunks
    if len(in_string) % num_chunks: chunk_size += 1
    iterator = iter(in_string)
    for _ in range(num_chunks):
        accumulator = list()
        for _ in range(chunk_size):
            try: accumulator.append(next(iterator))
            except StopIteration: break
        yield ''.join(accumulator)

textSects = list(chunk(fullText,4))    #creates the number of sections we want, stored in a list item

#TODO: process text w/ textProcessing tools to diff. lists using diff. functions
txtProcessor = TextProcessing()

#TODO: Awareness profile
def awarenessProfile (input_text):
    awarenessList = []
    fullTxtSumm = txtProcessor.summarizeText(fullText)  #summarizes full text
    awarenessList.append(fullTxtSumm)
    #topicizize the rest of the text
    for i in input_text:
        awarenessList.append(txtProcessor.topicizeText(i))
    
    return awarenessList

result = awarenessProfile(textSects)
counter = 0
for i in result:
    print(result[counter],'\n')

    counter += 1

##TODO: Professional profile
#TODO: Future Planning Profile

#TODO: create arrays to store text objs