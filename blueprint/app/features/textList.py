#TODO: Create a program that will create a list out of a body of text. 
from transformers import pipeline

topicizer = pipeline('summarization', model='tennessejoyce/titlewave-t5-base')

body = "Romeo and Juliet by William Shakespeare is the story of young lovers trying their best to live a happy life but can’t since they come from opposite families being the Montague and Capulet. During their trying to be together they end up knowing the only way to stay together was to take both their lives, but to who is to blame? The Capulet family or the Montague family was Friar Lawrence’s vial defective, is he to blame? But the one to blame for Romeo and Juliet’s death is no one other than Romeo and Juliet’s own ignorant actions because one the fact that both Romeo and Juliet are young teenagers with little to no experience, two they are too hasty during the story their love went by too fast, three they are to blind to find a breakeven solution and decide to go against everything they were raised for. So was it really their parents fault? Was it the family feud?  Friar Lawrence? No Romeo and Juliet died by their own actions it was an option to die no forced upon, they died by their own hands and no other is to be blamed."

print(topicizer(body))