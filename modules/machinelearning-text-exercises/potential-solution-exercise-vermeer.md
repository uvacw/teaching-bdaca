# Potential solution belong to [morning exercise](exercise-morning.md) with data of Vermeer

```python
import sys
import csv

csv.field_size_limit(sys.maxsize)


def get_data(t='test'):
    text= []
    label= []

    with open(f'data/{t}.csv') as fi:
        next(fi)
        reader = csv.reader(fi, delimiter=',')
        for row in reader:
            text.append(row[0])
            label.append(row[1])

    return text, label

X_test, y_test = get_data('test')
X_train, y_train = get_data('train')

from sklearn.svm import SVC

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
