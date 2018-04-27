import numpy as np
from sklearn import svm
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

data = np.array(list(csv.reader(open("noise_nonoise.csv"))))
f = open("inputtext.txt","r")

act_target = data[1:,0]
text = data[1:,1]

noise_t = np.where(act_target=="noise", 1,-1)

#target is ready. We need to restructure the text now into features.
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(text)
print(count_vect.get_feature_names())


tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf)


#Train
clf = svm.SVC(kernel='linear')
clf.fit(X_train_tfidf,noise_t)

#New Instance
test_text=[]
if f.mode == "r":
	f1 = f.readlines()
	for x in f1:
		test_text.append(x)
		

X_new_counts = count_vect.transform(test_text)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for i in range(3):
    print("Text:", test_text[i], "...Classification:","not noise\n" if predicted[i] == -1 else "noise\n")
