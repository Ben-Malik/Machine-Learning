from nltk import pos_tag,word_tokenize
article = open("love.txt", "r") 
abstract_file = open("100-400.txt", "r")
concrete_file = open("400-700.txt", "r")
subsective_file = open("subjectives.tff", "r")

def getWordSubjectiveness(word): 
    output = "None"
    for line in subsective_file.readlines():
        current = line.split()
        currentWord = current[2].split("=")[1]
        if (word.lower() == currentWord):
            output = current[0].split("=")[1]
            break
    return output

class Word:
    def __init__(self, w, w_pos, before_1_pos, before_2_pos, after_1_pos, after_2_pos):
        self.w = w
        self.w_pos = w_pos
        self.before_1_pos = before_1_pos
        self.before_2_pos = before_2_pos
        self.after_1_pos = after_1_pos
        self.after_2_pos = after_2_pos
    
    def toString(self): 
        return self.before_1_pos + " <-- " + self.before_2_pos + " <- " + self.w + " - " + self.w_pos + ' -> ' + self.after_1_pos + " --> " + self.after_2_pos

class Sentence:
    def __init__(self, words):
        self.sentence = list()
        for word in words:
            self.sentence.append(word)
    def __init__(self):
        self.sentence = list()

    def addWord(self, word):
        self.sentence.append(word)

    def toString(self): 
        for word in self.sentence:
            print(word.toString())
sentences = list()
abstract_words = list()
concrete_words = list()

for line in article.readlines():
    current = line.strip().split(' ')
    output = list()
    for word in current:
        word = word.strip(',.()\'\"').upper()
        output.append(word)
    sentences.append(output)

allSentences = list()
#Pos for each word
for i in range(len(sentences)):
    sentence = Sentence()
    for j in range(len(sentences[i])):
        before_1 = "No Before 1"
        before_2 = "No Before 2"
        after_1 = "No After 1"
        after_2 = "No After 2"
        output = list()
        word = pos_tag(word_tokenize(sentences[i][j]))[0][1]
        if (i == 0):
            if (j == 0):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
            elif (j == 1):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]
            elif (j == len(sentences[i])-1):
                after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
            elif (j == len(sentences[i])-2):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
            else: 
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]   
        elif (i == len(sentences)-1 and j == len(sentences[i])-1):
            before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
            before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
        elif (i == len(sentences)-1 and j == len(sentences[i])-2):
            before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
            before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
            after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
        else: 
            if (j == 0): 
                before_1 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
            elif (j == 1):
                before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
            elif (j == len(sentences[i])-1):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]
            elif ( j == len(sentences[i])-2):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
            else: 
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
        myWord = Word(sentences[i][j], word, before_1, before_2, after_1, after_2)
        sentence.addWord(myWord)
    allSentences.append(sentence)
       
        
print(getWordSubjectiveness('Hello'))