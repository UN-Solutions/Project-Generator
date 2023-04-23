#TODO: CREATE A PROGRAM THAT TAKES IN A STRING PARAMETER, PARSE AND SUMMARIZE THE TEXT
#THEN RETURN THE SUMMARIZED TEXT
from transformers import pipeline

summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")
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
        results = summarizer(sampleText)
        for results in results:
            return(results['summary_text'])

# minor testing
if __name__ == "__main__":
    #initialize the model
    #summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")

    #ask user for input
    #path = input('File path: ')
    path = '/home/migui/school/spring23/seniorXp/project/Project-Generator/data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
    result = SummarizeText(path)
    print(result.summarizeText())