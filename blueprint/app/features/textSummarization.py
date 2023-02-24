from happytransformer import HappyTextToText

# import from happytransfomers
from happytransformer import HappyTextToText

# load in huggingface model
# only uncomment if model has not downloaded

happy_tt = HappyTextToText("BART", "lidiya/bart-large-xsum-samsum")

# TODO: get text object to process the text summarization
with open ('data/sampleTexts/MSalvador_FinalPromptAssesment.txt') as f:
    sampleText = f.read()

# print(sampleText)
# output results from summarization including summarized text
transformerSampletext = happy_tt.generate_text(sampleText)
print(transformerSampletext)
print("\nThe summarized text of the sampled text is:\n",transformerSampletext.text)

