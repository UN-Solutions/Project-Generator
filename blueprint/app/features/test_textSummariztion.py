from transformers import pipeline
from textSummarization import SummarizeText

#summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")
#miniTesting
path = '/home/migui/school/spring23/seniorXp/project/Project-Generator/data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
s1 = SummarizeText(path)
#s1.summarizeText()
sumText = s1.summarizeText()
print(sumText)

##print out results to a txt file
#with open("/home/migui/school/spring23/seniorXp/project/Project-Generator/data/sampleTexts/oneThreeResult.txt",'w') as f:
    #f.write(str(result))
    #f.close




#summ = pipeline("summarization", model='lidiya/bart-large-xsum-samsum')
#path = '/home/migui/school/spring23/seniorXp/project/Project-Generator/data/sampleTexts/MSalvador_FinalPromptAssesment.txt'
#with open(path) as f:
    #text = f.read()
    #f.close()

#results = summ(text)
#for results in results:
    #print(results['summary_text'])
