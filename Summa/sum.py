from summa.summarizer import summarize
from summa import keywords

f1 = open("text.txt", "r")
f2 = open("summary.txt", "w")
f3 = open("feature.txt", "w")
content = f1.read()

f2.write(summarize(content, ratio = 0.2))

f3.write(keywords.keywords(content))


f1.close()