from summa.summarizer import summarize
from summa import keywords
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

st = LancasterStemmer()
l = WordNetLemmatizer()
word = set()

f1 = open("text.txt", "r", encoding="utf8")
f2 = open("summary.txt", "w")
f3 = open("feature.txt", "r+")
f4 = open("important_points.txt", "w")


content = f1.read()
f2.write(summarize(content, ratio = 0.2))
f3.write(keywords.keywords(content))

for line in f3:
    word.add(l.lemmatize(line[:-1]))

for i in word:
    f4.write(i)
    f4.write("\n")

f1.close()
f2.close()
f3.close()
f4.close()