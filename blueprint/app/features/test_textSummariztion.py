from transformers import pipeline
from textSummarization import SummarizeText

summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")
#miniTesting
path = '/home/migui/school/spring23/seniorXp/project/Project-Generator/data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
s1 = SummarizeText(path)
s1.summarizeText()