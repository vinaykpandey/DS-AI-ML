import nltk
import nltk.corpus
import os
#tokenize example
from nltk.tokenize import word_tokenize

input_string = "I am learing python"
wt = word_tokenize(input_string)
print(wt)



print(os.listdir(nltk.data.find("corpora")))


nltk.corpus.gutenberg.fileids()

hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
hamlet

AI = """According to the father of Artificial Intelligence, John McCarthy, it is “The science and engineering of making intelligent machines, especially intelligent computer programs”.

Artificial Intelligence is a way of making a computer, a computer-controlled robot, or a software think intelligently, in the similar manner the intelligent humans think.

AI is accomplished by studying how human brain thinks, and how humans learn, decide, and work while trying to solve a problem, and then using the outcomes of this study as a basis of developing intelligent software and systems.

"""
print(type(AI))
AI_tokens = word_tokenize(AI)
AI_tokens
len(AI_tokens)

from nltk.probability import FreqDist
fdist = FreqDist()
for word in AI_tokens:
    fdist[word.lower()] += 1

fdist
fdist_top10 =  fdist.most_common(10)
fdist_top10

from nltk.tokenize import blankline_tokenize
AI_blank = blankline_tokenize(AI)
len(AI_blank)

from nltk.util import bigrams, trigrams, ngrams
string = "The best and most beautiful things in the worlds cannot be seen or even touched, they must be felt with the heart"
q_tokens = word_tokenize(string)
q_tokens

q_bigrams = list(bigrams(q_tokens))
q_bigrams

q_trigrams = list(trigrams(q_tokens))
q_trigrams

q_ngrams = list(ngrams(q_tokens, 5))
q_ngrams

# stemming -> normalize words into base/root form
from nltk.stem import PorterStemmer, LancasterStemmer
pst = PorterStemmer()
lst = LancasterStemmer()
print(pst.stem('having'), lst.stem('having'))

words_to_stem = ["give", "given", "giving", "gave"]
for word in words_to_stem:
    print(word + ": " + pst.stem(word))

words_to_stem = ["give", "given", "giving", "gave"]
for word in words_to_stem:
    print(word + ": " + lst.stem(word))


# Lemmatization
from nltk.stem import wordnet, WordNetLemmatizer
lmt = WordNetLemmatizer()

words_to_stem = ["give", "given", "giving", "gave"]
for word in words_to_stem:
    print(word + ": " + lmt.lemmatize(word))

    

