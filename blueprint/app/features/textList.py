#TODO: Create a program that will create a list out of a body of text. 
from transformers import pipeline

topicizer = pipeline('summarization', model='tennessejoyce/titlewave-t5-base')

body = "In what is now New Mexico there used to house the Pueblo Indians, or the Zuni people. A tribe that believed everything is connected with one another and generally lived in peace and tranquility. However, it was in May 1539 that history took the helm and alter the lives of the Zuni. A Spanish group lead by Estavanico, were on a quest to find the “Seven Cities of Cibola”, where he alone went to investigate the Zuni city. The Zuni, however, did not have the hidden riches Estavanico, thought they were hiding, his advances got him killed. After the Spanish knew of Estavanicos death it only enflamed the rumors of the Cibola cities and raced to the Zuni town and pillaged the tribe. After all these years, the Zuni people are still here and share their stories and culture to upcoming young, even after tragedy they have their identity and thrive on their culture that was not able to been killed.After facing such tragedy the lingering question of how is it that the Zuni people are able to keep their culture alive? This video begins with the narrator telling us the story of how the Zuni people came to be, how they emerged from the dirt. The narrator does not say how the Zuni culture was kept alive but instead shows us just like in the intro, a tale of the people of Zuni. This video in itself aids with keeping the Zuni culture alive, throughout the video we hear the stories of folk, historic moments, and traditions. We see an elder later in the video that tells the tale of a Giant"

print(topicizer(body))