import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def summarize(sentences):
    sentence_value_table = {}
    sum_values = 0
    summary = ''
    for sentence in sentences:
        table = create_freq_table(sentence)
        for word in table:
            if word in sentence.lower():
                if sentence in sentence_value_table:
                    sentence_value_table[sentence] += table[word]
                else:
                    sentence_value_table[sentence] = table[word]

    # creates an average score for sentences
    for sentence in sentence_value_table:
        sum_values += sentence_value_table[sentence]
    average = int(sum_values / len(sentence_value_table))

    # Cosine similarity used to determine which sentences make it to the summary
    for sentence in sentences:
        if (sentence in sentence_value_table) and (sentence_value_table[sentence] > (1.2 * average)):
            summary += sentence + ' '

    return summary


def create_freq_table(image_text_list):
    # generates frequency table from words and removes stop words (words that add no meaning to the sentence)
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
    return freq_table
    # creates an array of sentences
