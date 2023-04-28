from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def text_summarizer(image_text_list):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(image_text_list)
    freq_table = dict()

    sentences = sent_tokenize(image_text_list)
    sentence_value = dict()