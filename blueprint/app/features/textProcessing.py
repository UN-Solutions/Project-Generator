from transformers import pipeline

# initialize transformers that will be utilized
summarizer = pipeline('summarization', model = 'lidiya/bart-large-xsum-samsum')     # model to summarize text
topicizer = pipeline('summarization', model='tennessejoyce/titlewave-t5-base')      # model to make topic out of text

# TODO: create classes to process text by summarizing and listing
class TextProcessing:
    """text input"""
    def __init__(self, genText):
        self.genText = genText

    """function to summarize text"""
    def summarizeText(self):
        result = summarizer(self.genText)
        for result in result:
            return(result['summary_text'])

    # TODO: function to list text
    
    """function to generate topic question of a given"""
    def topicizeText(self):
        result = topicizer(self.genText)
        for result in result:
            return(result['summary_text']) #limited to tokens (1024>512)
    
if __name__=="__main__":
    print("hello world")

