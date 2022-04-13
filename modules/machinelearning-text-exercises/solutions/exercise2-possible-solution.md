# Potential solution belong to [exercise 2](../README.md) with data of Vermeer

```python
import sys
import csv
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import metrics

csv.field_size_limit(sys.maxsize)


def get_labeled_data(fn='labeled.csv'):
    text= []
    label= []

    with open(fn) as fi:
        next(fi)
        reader = csv.reader(fi, delimiter=',')
        for row in reader:
            text.append(row[0])
            label.append(row[1])
    return text, label

texts, labels = get_labeled_data()
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=.2)
print(len(y_train),  len(X_train), len(y_test),  len(X_test))

configurations = [('NB with Count', CountVectorizer(min_df=5, max_df=.5), MultinomialNB()),
                 ('NB with TfIdf', TfidfVectorizer(min_df=5, max_df=.5), MultinomialNB()),
                 ('LogReg with Count', CountVectorizer(min_df=5, max_df=.5), LogisticRegression(solver='liblinear')),
                 ('LogReg with TfIdf', TfidfVectorizer(min_df=5, max_df=.5), LogisticRegression(solver='liblinear')),
                 ('SVM with Count - rbf kernel', CountVectorizer(min_df=5, max_df=.5), SVC(kernel='rbf')),
                 ('SVM with Count - linear kernel', CountVectorizer(min_df=5, max_df=.5), SVC(kernel='linear')),
                 ('SVM with Tfidf - rbf kernel', TfidfVectorizer(min_df=5, max_df=.5), SVC(kernel='rbf')),
                 ('SVM with Tfidf - linear kernel', TfidfVectorizer(min_df=5, max_df=.5), SVC(kernel='linear')),

                 ]

for description, vectorizer, classifier in configurations:
    print(description)
    X_tr = vectorizer.fit_transform(X_train)
    X_te = vectorizer.transform(X_test)
    classifier.fit(X_tr, y_train)
    y_pred = classifier.predict(X_te)
    print(metrics.classification_report(y_test, y_pred) )
    print('\n')
```


    
## Let's re-train and use one of the classifiers!

```python
def get_unlabeled_data(fn='unlabeled.csv'):
    text= []
    with open(fn) as fi:
        next(fi)
        for row in fi:
            text.append(row.strip())
    return text


unlabeled = get_unlabeled_data()

myvec = TfidfVectorizer(min_df=5, max_df=.5)
myclf = SVC(kernel='linear')
X_tr = myvec.fit_transform(X_train)
X_unlabeled = myvec.transform(unlabeled)
myclf.fit(X_tr, y_train)

y_pred = myclf.predict(X_unlabeled)

with open("predictions.csv" , mode='w') as fo:
    writer = csv.writer(fo)
    writer.writerows(zip(unlabeled,y_pred))


```
