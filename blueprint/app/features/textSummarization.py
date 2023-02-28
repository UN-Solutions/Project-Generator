#TODO: CREATE A PROGRAM THAT TAKES IN A STRING PARAMETER, PARSE AND SUMMARIZE THE TEXT
#THEN RETURN THE SUMMARIZED TEXT
from transformers import pipeline

#Class that will summarize the text
class SummarizeText:
    """API generated data info"""
    def __init__(self, genText):
        self.genText = genText

    """open up txt file w/ generated text, parse and summarize"""
    def summarizeText(self):
        with open(self.genText) as f:
            sampleText = f.read()
            f.close
        #print ('\n',sampleText)
        print(summarizer(sampleText))


    
##minor testing
if __name__ == "__main__":
    #initialize the model
    summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")

    #ask user for input
    path = input('File path: ')
    result = SummarizeText(path)
    result.summarizeText()