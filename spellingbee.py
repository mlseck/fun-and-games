from nltk.corpus import words

def split(word):
    return [char for char in word]

#Variable initialization
answers = []
alphabet = split('abcdefghijklmnopqrstuvwxyz')
allowed = split('imarujn')
compulsory = 'i'
for al in allowed:
    alphabet.remove(al)

#Keep 4+ letter words that contain the center letter
for word in words.words():
    if len(word)>=4 and compulsory in word:
        answers.append(word)

#Remove words that contain any letter that's not in
#authorized list
for word in answers:
    for letter in alphabet:
        if letter in word.lower():
            answers.remove(word)
            break