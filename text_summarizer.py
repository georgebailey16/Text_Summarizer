from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def summarize(image_text_list):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(image_text_list)
    freq_table = dict()
    sentences = sent_tokenize(image_text_list)
    sentence_value_table = dict()
    sum_values = 0
    summary = ''

    # generates frequency table from words and removes stop words (words that add no meaning to the sentence)
    for word in words:
        word = word.lower()
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

    # creates an array of sentences
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value_table:
                    sentence_value_table[sentence] += freq
                else:
                    sentence_value_table[sentence] = freq

    # creates an average score for sentences
    for sentence in sentence_value_table:
        sum_values += sentence_value_table[sentence]
    average = int(sum_values / len(sentence_value_table))

    # Cosine similarity used to determine which sentences make it to the summary
    for sentence in sentences:
        if (sentence in sentence_value_table) and (sentence_value_table[sentence] > (1.2 * average)):
            summary += sentence + ' '

    return summary
