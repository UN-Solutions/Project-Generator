#TODO: Driver module that takes in text and outputs the various objects into a file
#from textProcessing import TextProcessing

# read in file 
path = '/home/msalvador45/school/spring23/seniorXP/project/Project-Generator/data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
with open(path) as f:
    ogText = f.read()
    f.close()

ogText = ogText.split() #create a list out of the text
print(ogText)
print(len(ogText))

# Throw exceptions for insufficient word lenght or too much word length

if len(ogText) < 100 :
    raise Exception('text document is less than 100 words, need text document (100<length<2400)')
elif len(ogText) > 2400:
    raise Exception('text document is more than 2400 words, need text document (100<length<2400)')
else:
    print('text document is between 100 and 2400 words')
    fullText = ' '.join(ogText)
    print(fullText)
    
#TODO: create diff arrays oAr strings to make partitions

#TODO: process text w/ textProcessing tools

#TODO: create arrays to store text objs