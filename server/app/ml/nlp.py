import enchant
import nltk
import string
def cleanText(text):
    d = enchant.Dict("en_US")
    final_text = []
    text = text.split('\n')
    for sentence in text:
        words = sentence.split()
        new_sentence = []
        for word in words:
            # removing punctuation
            clean_word = word.translate(str.maketrans('', '', string.punctuation)).strip()
            word = word.strip()
            if word.lower() == "a" or word.lower() == "i":
                new_sentence.append(word)
            elif len(word) > 1: 
                try: 
                    if (d.check(word) or d.check(clean_word)):
                        new_sentence.append(word)
                    elif nltk.edit_distance(d.suggest(clean_word)[0], clean_word) <= 2:
                        new_sentence.append(d.suggest(word)[0])
                except Exception:
                    continue
        if new_sentence != []:
            if len(new_sentence) == len(words):
                final_text = final_text + [" ".join(new_sentence)]
            else:
                final_text = final_text + [" ".join(new_sentence)]
    return " ".join(final_text)