#TODO: Driver module that takes in text and outputs the various objects into a file
#from textProcessing import TextProcessing

# read in file 
path = '/home/msalvador45/school/spring23/seniorXP/project/Project-Generator/data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
with open(path) as f:
    fullText = f.read()
    f.close()
 
print(len(fullText))

#TODO: create diff arrays or strings to make partitions

#TODO: process text w/ textProcessing tools

#TODO: create arrays to store text objs