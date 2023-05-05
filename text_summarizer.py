import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def summarize2(image_text_list):
    sentence_value_table = {}
    sum_values = 0
    summary = ''
    words = word_tokenize(image_text_list)
    stop_words = set(stopwords.words("english"))
    freq_table = {}

    for word in words:
        word = word.lower()
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

    sentences = sent_tokenize(image_text_list)

    for sentence in sentences:
        for word in freq_table:
            if word in sentence.lower():
                if sentence in sentence_value_table:
                    sentence_value_table[sentence] += freq_table[word]
                else:
                    sentence_value_table[sentence] = freq_table[word]

    # creates an average score for sentences
    for sentence in sentence_value_table:
        sum_values += sentence_value_table[sentence]
    average = int(sum_values / len(sentence_value_table))

    # Cosine similarity used to determine which sentences make it to the summary
    for sentence in sentences:
        if (sentence in sentence_value_table) and (sentence_value_table[sentence] > (1.2 * average)):
            summary += sentence + ' '

    return summary
