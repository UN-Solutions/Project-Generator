from transformers import pipeline
from textSummarization import SummarizeText

#summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")
#miniTesting
path = '/home/migui/school/spring23/seniorXp/project/Project-Generator/data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
s1 = SummarizeText(path)
#s1.summarizeText()
result = s1.summarizeText()
print("\n", str(result))

#print out results to a txt file
with open("/home/migui/school/spring23/seniorXp/project/Project-Generator/data/sampleTexts/oneThreeResult.txt",'w') as f:
    f.write(str(result))
    f.close
