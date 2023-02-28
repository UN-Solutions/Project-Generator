from transformers import pipeline
from textSummarization import SummarizeText

#summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")
#miniTesting
path = '/home/msalvador45/school/spring23/seniorXP/project/Project-Generator/data/sampleTexts/oneTwo.txt'
s1 = SummarizeText(path)
s1.summarizeText()