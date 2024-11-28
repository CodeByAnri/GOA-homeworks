
# Manual Capital

def Capital(sentence):
    sentence_alt = ""
    for i in range(len(sentence)):
        if i == 0:
            sentence_alt += sentence[i].upper()
        else: sentence_alt += sentence[i]
    print(sentence_alt)


sentence = str(input("Enter The Sentence: " ))


Capital(sentence)

# Manual Title

def Title(sentence):
    sentence = sentence.split()
    sentence_alt = []
    for word in sentence:
        word_alt = " "
        for i in range(len(word)):
            if i == 0:
                word_alt += word[i].upper()
            else: word_alt += word[i]
        sentence_alt.append(word_alt)
    sentence_alt = " ".join(sentence_alt)
    print(sentence_alt)

sentence = str(input("Enter The Sentence: " ))


Title(sentence)


