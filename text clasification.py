from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
import nltk

# nltk.download('punkt')

training_corpus=[
    ('I am exhausted of this work','class_B'),
    ('I can\'t cooperate with this','class_B'),
    ('He is my enemy','class_B'),
    ('My Manager is poor','class_B'),
    ('I love to eat food','class_A'),
    ('This is my good job','class_A'),
    ('I am good in python','class_A')
]

test_corpus=[
    ('I am not feeling well today','class_B'),
    ('I feel good','class_A'),
    ('Amit is my friend','class_A')
]

model=NBC(training_corpus)
print(model.classify('I dont\'t like smoking'))
print(model.accuracy(test_corpus))