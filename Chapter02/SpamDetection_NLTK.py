import nltk
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from collections import Counter
from nltk import NaiveBayesClassifier, classify

def Process(data):
  lemmatizer = WordNetLemmatizer()
  return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode(sentence,errors='ignore'))]
 

def Features_Extraction(text, setting):
  if setting=='bow':
   # Bow means bag-of-words
    return {
        word: count
        for word, count in Counter(Process(text)).items() if word not in stop
    }
  else:
    return {word: True for word in Process(text) if word not in stop}
    
features = [(Features_Extraction(email, 'bow'), label) for (email, label)
in emails]

def training_Model(Features, samples):
  Size = int(len(Features) * samples)
  training , testing = Features[:Size], Features[Size:]
  print(f'Training = {len(training)} emails')
  print(f'Testing = {len(testing)} emails')
  
classifier = NaiveBayesClassifier.train(training)

def evaluate(training, tesing, classifier):
  print(f'Training Accuracy is {str(classify.accuracy(classifier, train_set))}')
  print(f'Testing Accuracy i {str(classify.accuracy(classifier, test_set))}')





