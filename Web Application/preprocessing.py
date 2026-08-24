import nltk
import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# Create stemmer
ps = PorterStemmer()


def transform_text(data):

    # 1. Convert to lowercase
    data = data.lower()

    # 2. Tokenization
    data = nltk.word_tokenize(data)

    # 3. Keep only alphanumeric words
    lst = []

    for i in data:
        if i.isalnum():
            lst.append(i)

    data = lst[:]

    # 4. Remove stopwords and punctuation
    lst.clear()

    for i in data:
        if i not in stopwords.words('english') and i not in string.punctuation:
            lst.append(i)

    data = lst[:]

    # 5. Stemming
    lst.clear()

    for i in data:
        lst.append(ps.stem(i))

    # 6. Convert list back to string
    return " ".join(lst)