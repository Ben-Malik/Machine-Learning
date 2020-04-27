from nltk import pos_tag,word_tokenize
article = open("love.txt", "r") 
abstract_file = open("100-400.txt", "r")
concrete_file = open("400-700.txt", "r")

def getWordSubjectiveness(word): 
    output = "None"
    subsective_file = open("subjectives.tff", "r")
    for line in subsective_file.readlines():
        current = line.split()
        currentWord = current[2].split("=")[1]
        if (word.lower() == currentWord):
            output = current[0].split("=")[1]
            break
    return output

def isWordListedInNegative(word):
    isInPositive = False
    isInNegative = False
    wordFound = False
    senti_word_net_file = open("SentiWordNet_3.0.0.txt", "r")

    for line in senti_word_net_file.readlines():
        current = line.split("\t")
        words = current[4].split(' ')
        for i in range(len(words)):
            if (words[i].split("#")[0] == word.lower()):
                if (current[2]!='0'):
                        isInPositive = True
                if (current[3]!='0'):
                    isInNegative = True
            wordFound = True
            break
        if (wordFound == True):
            break

    return (isInNegative, isInPositive)

class Word:
    def __init__(self, w, w_pos, before_1_pos, before_2_pos, after_1_pos, after_2_pos, is_positive, is_negative, is_before_1_positive, is_before_1_negative, is_before_2_positive, is_before_2_negative, is_after_1_positive, is_after_1_negative, is_after_2_positive, is_after_2_negative):
        self.w = w
        self.w_pos = w_pos
        self.before_1_pos = before_1_pos
        self.before_2_pos = before_2_pos
        self.after_1_pos = after_1_pos
        self.after_2_pos = after_2_pos
        self.is_negative = is_negative
        self.is_positive = is_positive
        self.is_after_1_positive = is_after_1_positive
        self.is_after_1_negative = is_after_1_negative
        self.is_after_2_positive = is_after_2_positive
        self.is_after_2_negative = is_after_2_negative
        #Before
        self.is_before_1_positive = is_before_1_positive
        self.is_before_1_negative = is_before_1_negative
        self.is_before_2_positive = is_before_2_positive
        self.is_before_2_negative = is_before_2_negative
    
    def toString(self): 
        return self.before_1_pos + " <-- " + self.before_2_pos + " <- " + self.w + " - " + self.w_pos + ' -> ' + self.after_1_pos + " --> " + self.after_2_pos
    
    def toPositivenessString(self):
        return self.is_before_2_positive , self.is_before_1_positive , self.w , self.is_positive , self.is_after_1_positive , self.is_after_2_positive
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
            print(word.toPositivenessString())
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
        word_before_1 = ""
        word_before_2 = ""
        word_after_1 = ""
        word_after_2 = ""
        output = list()
        word = pos_tag(word_tokenize(sentences[i][j]))[0][1]
        if (i == 0):
            if (j == 0):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                word_after_1 = sentences[i][j+1]
                word_after_2 = sentences[i][j+2]
            elif (j == 1):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]

                word_after_1 = sentences[i][j+1]
                word_after_2 = sentences[i][j+1]
                word_before_1 = sentences[i][0]
            elif (j == len(sentences[i])-1):
                after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]

                word_after_1 = sentences[i+1][0]
                word_after_2 = sentences[i+1][1]
                word_before_1 = sentences[i][j-1]
                word_before_2 = sentences[i][j-2]
            elif (j == len(sentences[i])-2):
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]

                word_after_1 = sentences[i][j+1]
                word_after_2 = sentences[i+1][0]
                word_before_1 = sentences[i][j-1]
                word_before_2 = sentences[i][j-2]
            else: 
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]   

                word_after_1 = sentences[i][j+1]
                word_after_2 = sentences[i][j+2]
                word_before_1 = sentences[i][j-1]
                word_before_2 = sentences[i][j-2]
        elif (i == len(sentences)-1 and j == len(sentences[i])-1):
            before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
            before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]

            word_before_1 = sentences[i][j-1]
            word_before_2 = sentences[i][j-2]
        elif (i == len(sentences)-1 and j == len(sentences[i])-2):
            before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
            before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
            after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]

            word_before_1 = sentences[i][j-1]
            word_before_2 = sentences[i][j-2]
            word_after_1 = sentences[i][j+1]
        else: 
            if (j == 0): 
                before_1 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]

                before_word_1 = sentences[i-1][len(sentences[i-1])-1]
                before_word_2 = sentences[i-1][len(sentences[i-1])-2]
                after_word_1 = sentences[i][j+1]
                after_word_2 = sentences[i][j+2]
            elif (j == 1):
                before_1 = pos_tag(word_tokenize(sentences[i][0]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i-1][len(sentences[i-1])-1]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]

                before_word_1 = sentences[i][0]
                before_word_2 = sentences[i-1][len(sentences[i-1])-1]
                after_word_1 = sentences[i][j+1]
                after_word_2 = sentences[i][j+2]
            elif (j == len(sentences[i])-1):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][1]))[0][1]

                before_word_1 = sentences[i][j-1]
                before_word_2 = sentences[i][j-2]
                after_word_1 = sentences[i+1][0]
                after_word_2 = sentences[i+1][1]
            elif ( j == len(sentences[i])-2):
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i+1][0]))[0][1]

                before_word_1 = sentences[i][j-1]
                before_word_2 = sentences[i][j-2]
                after_word_1 = sentences[i][j+1]
                after_word_2 = sentences[i+1][0]
            else: 
                before_1 = pos_tag(word_tokenize(sentences[i][j-1]))[0][1]
                before_2 = pos_tag(word_tokenize(sentences[i][j-2]))[0][1]
                after_1 = pos_tag(word_tokenize(sentences[i][j+1]))[0][1]
                after_2 = pos_tag(word_tokenize(sentences[i][j+2]))[0][1]

                before_word_1 = sentences[i][j-1]
                before_word_2 = sentences[i][j-2]
                after_word_1 = sentences[i][j+1]
                after_word_2 = sentences[i][j+2]

        is_positive = isWordListedInNegative(sentences[i][j])[1]
        is_negative = isWordListedInNegative(sentences[i][j])[0]  

        is_word_before_1_positive = isWordListedInNegative(word_before_1)[1]
        is_word_before_1_negative = isWordListedInNegative(word_before_1)[0]

        is_word_before_2_positive = isWordListedInNegative(word_before_2)[1]
        is_word_before_2_negative = isWordListedInNegative(word_before_2)[0]

        is_word_after_1_positive = isWordListedInNegative(word_after_1)[1]
        is_word_after_1_negative = isWordListedInNegative(word_after_1)[0]

        is_word_after_2_positive = isWordListedInNegative(word_after_2)[1]
        is_word_after_2_negative = isWordListedInNegative(word_after_2)[0] 
 
        myWord = Word(sentences[i][j], word, before_1, before_2, after_1, after_2, is_positive, is_negative, is_word_before_1_positive, is_word_before_1_negative, is_word_before_2_positive, is_word_before_2_negative, is_word_after_1_positive, is_word_after_1_negative, is_word_after_2_positive, is_word_after_2_negative)
        sentence.addWord(myWord)
    allSentences.append(sentence)
       
        
for sentence in allSentences:
    print(sentence.toString())